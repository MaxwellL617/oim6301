"""
make_data.py
Generates CSV files for the BabsonAI Labs database.
as_of date: 2026-11-07
Covers 12 months: 2025-11-07 to 2026-11-07
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

AS_OF = date(2026, 11, 7)
START = date(2025, 11, 7)

# ── helpers ──────────────────────────────────────────────────────────────────

def rand_date(lo, hi):
    delta = (hi - lo).days
    return lo + timedelta(days=random.randint(0, delta))

def write_csv(name, rows, fieldnames):
    path = DATA_DIR / f"{name}.csv"
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {path} ({len(rows)} rows)")

# ── PEOPLE (25 people, self-referential manager) ──────────────────────────────

first_names = [
    "Ava","Ben","Cara","Diego","Elena","Finn","Grace","Hiro",
    "Isla","Jake","Kira","Leo","Maya","Nate","Olivia","Paul",
    "Quinn","Rosa","Sam","Tara","Uma","Vince","Wren","Xander","Yara"
]
last_names = [
    "Adams","Brown","Chen","Davis","Evans","Foster","Garcia","Hill",
    "Ito","Jones","Kim","Lee","Marsh","Nguyen","Ortiz","Patel",
    "Quinn","Rivera","Smith","Tran","Ueda","Vega","Walsh","Xu","Yoon"
]

titles = [
    "Founder","Founder",
    "VP Engineering","VP Product",
    "Senior Engineer","Senior Engineer","Senior Engineer",
    "Engineer","Engineer","Engineer","Engineer","Engineer",
    "Senior Data Scientist","Data Scientist","Data Scientist",
    "Senior PM","PM","PM",
    "Designer","Designer",
    "Operations Lead","Operations Analyst",
    "Sales Lead","Sales Analyst","Intern"
]

# manager_id: founders (1,2) report to nobody; others report upward
# person_id 1-indexed
people = []
for i, (fn, ln, title) in enumerate(zip(first_names, last_names, titles), start=1):
    start_date = rand_date(START - timedelta(days=365), START + timedelta(days=180))
    if i <= 2:
        manager_id = ""  # founders
    elif i <= 4:
        manager_id = random.choice([1, 2])
    elif i <= 12:
        manager_id = 3   # report to VP Eng
    elif i <= 15:
        manager_id = 3   # Senior DS and DS report to VP Eng
    elif i <= 18:
        manager_id = 4   # Senior PM and PMs report to VP Product
    elif i <= 20:
        manager_id = 4   # report to VP Product
    elif i <= 22:
        manager_id = 1   # Ops Lead and Analyst report to Founder 1
    elif i <= 24:
        manager_id = 2   # Sales Lead and Analyst report to Founder 2
    else:
        manager_id = random.choice([3, 4, 16])

    email = f"{fn.lower()}.{ln.lower()}@babsonailabs.com"
    people.append({
        "person_id": i,
        "first_name": fn,
        "last_name": ln,
        "work_email": email,
        "title": title,
        "start_date": start_date,
        "manager_id": manager_id,
    })

write_csv("people", people, ["person_id","first_name","last_name","work_email","title","start_date","manager_id"])

# ── PROJECTS (15 projects) ────────────────────────────────────────────────────

project_names = [
    "SmartChat Assistant","DataFlow Pipeline","Internal HR Bot",
    "RetailSense AI","HealthTrack Insights","Campus Navigator",
    "SupplyChain Optimizer","AutoReport Engine","TalentMatch AI",
    "EduAssist Platform","FraudGuard Model","Internal Expense Tracker",
    "LegalDoc Analyzer","SocialPulse Monitor","Internal DevOps Dashboard"
]
categories = ["LLM app","data pipeline","internal tool"]
statuses   = ["planned","active","active","active","paused","done"]
clients = [
    "RetailCo","HealthFirst","Babson College","SupplyNow Inc",
    "AutoCorp","TalentHub","EduTech LLC","SecureBank",
    "LegalEase","SocialBuzz","","","","",""
]  # last 5 are internal (no client)

projects = []
for i, name in enumerate(project_names, start=1):
    proj_start = rand_date(START, START + timedelta(days=300))
    budget = round(random.uniform(10000, 200000), 2)
    cat = categories[i % 3]
    status = random.choice(statuses)
    client = clients[i - 1] if i <= 10 else ""
    projects.append({
        "project_id": i,
        "name": name,
        "client_name": client,
        "category": cat,
        "budget": budget,
        "start_date": proj_start,
        "status": status,
    })

write_csv("projects", projects, ["project_id","name","client_name","category","budget","start_date","status"])

# ── PROJECT_MEMBERS ───────────────────────────────────────────────────────────

roles = ["Lead Engineer","Engineer","Data Scientist","PM","Designer","Analyst","Intern"]
project_members = []
pm_set = set()

for proj in projects:
    pid = proj["project_id"]
    # assign 3-7 people per project
    n = random.randint(3, 7)
    assigned = random.sample(range(1, 26), n)
    for person_id in assigned:
        if (person_id, pid) in pm_set:
            continue
        pm_set.add((person_id, pid))
        hours = random.randint(1, 40)
        joined = rand_date(proj["start_date"] if isinstance(proj["start_date"], date) else date.fromisoformat(str(proj["start_date"])), AS_OF)
        project_members.append({
            "person_id": person_id,
            "project_id": pid,
            "role": random.choice(roles),
            "hours_per_week": hours,
            "joined_date": joined,
        })

write_csv("project_members", project_members,
          ["person_id","project_id","role","hours_per_week","joined_date"])

# ── TASKS (250+) ──────────────────────────────────────────────────────────────

task_descriptions = [
    "Design system architecture","Write unit tests","Deploy to staging",
    "Review pull request","Update documentation","Fix login bug",
    "Optimize query performance","Build dashboard prototype","Client demo prep",
    "Data cleaning pipeline","Model fine-tuning","API integration",
    "Security audit","Write test cases","Conduct user interview",
    "Set up CI/CD","Performance benchmarking","Sprint planning",
    "Stakeholder update","Code review session",
]

tasks = []
task_id = 1

# build a lookup: project_id -> list of person_ids on that project
proj_people = {}
for pm in project_members:
    proj_people.setdefault(pm["project_id"], []).append(pm["person_id"])

for proj in projects:
    pid = proj["project_id"]
    n_tasks = random.randint(15, 25)
    workers = proj_people.get(pid, [])
    for _ in range(n_tasks):
        created = rand_date(START, AS_OF - timedelta(days=1))
        due = created + timedelta(days=random.randint(3, 60))
        # pick assignee from project members (or leave unassigned ~15%)
        if workers and random.random() > 0.15:
            assignee = random.choice(workers)
            # respect start_date rule
            person = next(p for p in people if p["person_id"] == assignee)
            person_start = person["start_date"]
            if isinstance(person_start, str):
                person_start = date.fromisoformat(person_start)
            if created < person_start:
                created = person_start + timedelta(days=1)
                due = created + timedelta(days=random.randint(3, 60))
        else:
            assignee = ""

        # completed_date: ~60% of tasks are done
        if random.random() < 0.6:
            completed = rand_date(created, min(due + timedelta(days=10), AS_OF))
        else:
            completed = ""

        tasks.append({
            "task_id": task_id,
            "project_id": pid,
            "description": random.choice(task_descriptions),
            "created_date": created,
            "assigned_to": assignee,
            "due_date": due,
            "completed_date": completed,
        })
        task_id += 1

# ── RULE BREAKS for tasks ─────────────────────────────────────────────────────
# Rule: assignee must work on the task's project
# Break it in exactly 2 rows: assign person NOT on the project

broken_task_ids = []
for t in tasks[-10:]:
    pid = t["project_id"]
    workers_on_proj = set(proj_people.get(pid, []))
    outsiders = [p["person_id"] for p in people if p["person_id"] not in workers_on_proj]
    if outsiders and t["assigned_to"] != "":
        t["assigned_to"] = random.choice(outsiders)
        broken_task_ids.append(t["task_id"])
    if len(broken_task_ids) == 2:
        break

print(f"\n  [RULE BREAK] Tasks where assignee does NOT work on the project: task_ids {broken_task_ids}")

write_csv("tasks", tasks,
          ["task_id","project_id","description","created_date","assigned_to","due_date","completed_date"])

# ── EXPENSES (150+) ───────────────────────────────────────────────────────────

expense_categories = ["GPU cloud","data labeling","software","travel"]
expenses = []
exp_id = 1

# Leave project_id 12 (Internal Expense Tracker) with NO expenses on purpose
no_expense_project = 12

for proj in projects:
    pid = proj["project_id"]
    if pid == no_expense_project:
        continue
    n_exp = random.randint(8, 18)
    for _ in range(n_exp):
        exp_date = rand_date(START, AS_OF)
        amount = round(random.uniform(50, 8000), 2)
        expenses.append({
            "expense_id": exp_id,
            "project_id": pid,
            "expense_date": exp_date,
            "amount": amount,
            "category": random.choice(expense_categories),
            "note": f"Expense for project {pid}",
        })
        exp_id += 1

print(f"\n  [INTENTIONAL] Project {no_expense_project} has no expenses (tests 'projects with no expenses' question)")
print(f"\n  Total tasks: {len(tasks)}, Total expenses: {len(expenses)}")

write_csv("expenses", expenses,
          ["expense_id","project_id","expense_date","amount","category","note"])

print("\nDone. All CSV files written to projects/db/data/")
