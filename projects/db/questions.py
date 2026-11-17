import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import duckdb
    from pathlib import Path

    database = mo.notebook_dir() / "database.duckdb"

    def ask(sql):
        with duckdb.connect(database, read_only=True) as _con:
            return _con.sql(sql).pl()

    return ask, database, mo


@app.cell
def _(ask):
    ask
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Prediction
    ###

    Based on the build.py file and how many items were in each of the tables I know that for question 6 there are a total of 15 projects with 292 tasks and 192 expenses. I would expect that I would need to join the tables together so that I can summarize the project data by expenses and tasks. If there are projects with no expenses and no tasks I might expect that that project might now show up depening on the type of join I do but assuming every project has at least one task or exense then I would expect to see all 1 projects with summarized data for expenses and tasks. I am going to group by project otherwise I would expect t o see 292 + 192 rows if I joined tasks and expenses without aggregating first.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Questions

    1. Each project's expenses against its budget, and the share of the budget spent, the largest share first.
    2. The tasks past their due date and not completed, with the project's name and the name of the person assigned. (three tables or more)
    3. Each person's hours a week across all active projects, and the people above 40.
    4. Expenses by category over the last 90 days, keeping only the categories whose total is above the average of the category totals.
    5. The projects with no expenses at all.
    6. One row per project with its number of tasks and its total expenses, each checked against counting it on its own. (three tables or more)
    7. Every task checked against the rule that its assignee works on its project, and a list of any that break it. (three tables or more) (checks a rule)
    8. For each manager, how many people report to them directly, and the hours a week those people have committed across all projects. (three tables or more)

    My questions
    1. What is the average lateness on a project, and which projects exceeded that amount and by how much
    2. What is the average project length, how many employees are assigned to it, and how many hours were spent on that project
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Question 1
    """)
    return


@app.cell
def _(ask):
    ask("""
    SELECT 
        name, 
        budget, 
        SUM(amount) AS total_expenses,
        ROUND(SUM(amount) / budget * 100, 2) AS share_of_budget
    FROM projects
    JOIN expenses USING (project_id)
    GROUP BY name, budget
    ORDER BY share_of_budget DESC
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Question 2
    """)
    return


@app.cell
def _(ask):
    ask("""SELECT last_name, name,description, due_date, completed_date, datediff('day',due_date, completed_date) as complete_diff_days
    from people
    join project_members using (person_id)
    join projects using (project_id)
    join tasks using (project_id)
    group by last_name,name,description ,due_date, completed_date""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Question 3
    """)
    return


@app.cell
def _(ask):
    ask("""SELECT first_name ||' '|| last_name as full_name,name,hours_per_week
    from people
    JOIN project_members using(person_id)
    JOIN projects using(project_id)
    where hours_per_week > 40
    group by full_name, name, hours_per_week
    order by full_name""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Question 4
    """)
    return


@app.cell
def _(ask):
    ask("""SELECT category,round(sum(amount), 2) as total_expenses
    FROM expenses
    WHERE expense_date >= date '2026-11-07' - interval '90' DAY
    GROUP BY category
    HAVING SUM(amount) > (
        SELECT AVG(cat_total)
        FROM (
            SELECT SUM(amount) AS cat_total
            FROM expenses
            WHERE expense_date >= DATE '2026-11-07' - INTERVAL '90' DAY
            GROUP BY category
        )
    )
    ORDER BY total_expenses DESC
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Question 5
    """)
    return


@app.cell
def _(ask):
    ask("""select name
    from projects
    left join expenses using(project_id)
    WHERE amount IS NULL""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Question 6

    One row per project with its number of tasks and its total expenses, each checked against counting it on its own. (three tables or more)
    """)
    return


@app.cell
def _(ask):
    ask("""SELECT name, project_id, count(distinct task_id) as task_count, round(sum( distinct amount),2) as total_expenses
    from projects
    join tasks using (project_id)
    join expenses using(project_id)
    group by name, project_id
    order by project_id asc""")
    return


@app.cell
def _(ask):
    # task count on its own
    ask("""
    SELECT project_id, COUNT(*) AS task_count
    FROM tasks
    GROUP BY project_id
    """)
    return


@app.cell
def _(ask):
    # expense total on its own
    ask("""
    SELECT project_id, ROUND(SUM(amount), 2) AS total_expenses
    FROM expenses
    GROUP BY project_id
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Question 7

    Every task checked against the rule that its assignee works on its project, and a list of any that break it. (three tables or more) (checks a rule)
    """)
    return


@app.cell
def _(ask):
    ask("""
    SELECT task_id, description, name, last_name, people.person_id, project_members.person_id 
    FROM tasks
    JOIN projects USING (project_id)
    JOIN people ON assigned_to = person_id
    LEFT JOIN project_members 
        ON assigned_to = project_members.person_id 
        AND tasks.project_id = project_members.project_id
    WHERE project_members.person_id IS NULL
    """)
    return


@app.cell
def _(ask):
    ask("""select name, task_id, description, assigned_to, last_name, person_id
    from projects 
    join tasks using (project_id)
    join people on (assigned_to = person_id)
    group by name, task_id, description, assigned_to, last_name, person_id""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Question 8

    For each manager, how many people report to them directly, and the hours a week those people have committed across all projects. (three tables or more)
    """)
    return


@app.cell
def _(ask):
    ask("""
    SELECT 
        managers.first_name || ' ' || managers.last_name AS manager_name,
        COUNT(reports.person_id) AS direct_reports,
        SUM(pm.hours_per_week) AS total_hours_per_week
    FROM people AS reports
    JOIN people AS managers ON reports.manager_id = managers.person_id
    JOIN project_members AS pm ON reports.person_id = pm.person_id
    GROUP BY managers.person_id, managers.first_name, managers.last_name
    ORDER BY manager_name
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    My Questions

    What is the average lateness on a project, and which projects exceeded that amount and by how much

    What is the average project length, how many employees are assigned to it, and how many hours were spent on that project
    """)
    return


@app.cell
def _(ask):
    ask("""
    SELECT 
        ROUND(AVG(DATEDIFF('day', p.start_date, t.completed_date)), 1) AS avg_days_to_complete
    FROM projects p
    JOIN tasks t USING (project_id)
    WHERE t.completed_date IS NOT NULL
    """)
    return


@app.cell
def _(ask):
    ask("""select name, datediff('day',p.start_date,t.completed_date) as days_to_complete
    from projects p
    join tasks t using (project_id)
    where days_to_complete < 72.3 """)
    return


@app.cell
def _(ask):
    ask("""select name, sum(hours_per_week) as avg_hours_per_week, count(distinct person_id) as assigned_employees,round(sum(hours_per_week)/count(distinct person_id),2) as avg_hours_per_person
    from projects
    join project_members using (project_id)
    join people using (person_id)
    group by name
    order by avg_hours_per_week desc""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##How I know These Numbers Are Right
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In question 6 after the query required by the question I seperetely calculated the count of projects and the sum of expenses seperetely to compare them to the originally query. At first it did not match but that was because I was organizing by project_id in the check and I was organizing by project name in the main query for question 6. After ordering them under the same conventions they all matched in just running a sum and count and doing both and aggregating them under one query

    The second piece I know is right is calculating the average project length before running the queries based on my questions. Instead of one very long complicated query trying to average all project lengths in all categories among all projects and all tasks I just calculated that seperetely and then incorporated that number into the query to see which ones were below the overall average
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Working With the Agent
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For question 1 I worked with the agent on a query where the result resulted in prject names repeating itself with this original query:

    SELECT name, budget, sum(amount) AS total_expenses, (amount/budget)*100 AS share_of_budget
    FROM projects
    inner join expenses using(project_id)
    GROUP BY name, budget, share_of_budget
    ORDER BY share_of_budget DESC

    I then asked the agent to adapt the query so that the project names would not be repeated and to round the share of budget to two decimal places and the resulting query was this:

    SELECT name,  budget,  SUM(amount) AS total_expenses, ROUND(SUM(amount) / budget * 100, 2) AS share_of_budget
    FROM projects
    JOIN expenses USING (project_id)
    GROUP BY name, budget
    ORDER BY share_of_budget DESC
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Reading It Back
    """)
    return


@app.cell
def _(ask):
    ask("""SELECT name, project_id, count(distinct task_id) as task_count, round(sum( distinct amount),2) as total_expenses
    from projects
    join tasks using (project_id)
    join expenses using(project_id)
    group by name, project_id
    order by project_id asc""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When reading my prediction for question 6 I think I got the prediction mostly right it did almost exactly what I though it would and aggregated the expenses and task count by the projects. The only thing i did not expect is that there are 15 project ids and all 15 are in the project table but there are only 14 unique ids in the task table so in the final table there are only 14 rows instead of 15, since the project that has no associated tasks does not appear in the merged result. project id 14 does not exist in expenses. The expenses tabledoes not have any matches for project with id 14 so the end product is dropping project id 14
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Going Further
    """)
    return


@app.cell
def _(ask):
    import polars as pl
    import matplotlib.pyplot as plt

    result = ask("""
    SELECT 
        name,
        ROUND(SUM(amount) / budget * 100, 2) AS share_of_budget
    FROM projects
    JOIN expenses USING (project_id)
    GROUP BY name, budget
    ORDER BY share_of_budget DESC
    """)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(result["name"], result["share_of_budget"])
    ax.set_xlabel("% of Budget Spent")
    ax.set_ylabel("Project")
    ax.set_title("Expenses as a Share of Budget by Project")
    ax.axvline(x=100, color="red", linestyle="--", label="Budget limit")
    ax.legend()
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    I though I would revisit question one and ask the ai agent to chart the projects that exceeded their limit by a percentage. It took the liberty of adding a threshold line in the middle to deonte what 100% of budget is but it is mainly a function of the second part of question one to ask which projects exceedd their budget or met their budget by what percentage and this just graphs it so you can visualize it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Time Spent
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    7 -hours
    """)
    return


@app.cell
def _(ask):
    ask("""SELECT count(*) FROM tasks""")
    return


@app.cell
def _(ask):
    ask("SELECT COUNT(*) FROM people")
    return


@app.cell
def _(database):
    print(database)
    return


@app.cell
def _(ask):
    ask("SHOW TABLES")
    return


@app.cell
def _(ask):
    ask("SELECT * FROM people LIMIT 3")
    return


if __name__ == "__main__":
    app.run()
