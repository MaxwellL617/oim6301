import marimo

__generated_with = "0.9.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import duckdb
    from pathlib import Path
    return duckdb, mo, Path


@app.cell
def __(mo, Path):
    database = mo.notebook_dir() / "database.duckdb"
    data_dir = mo.notebook_dir() / "data"

    def ask(sql):
        with duckdb.connect(database, read_only=True) as _con:
            return _con.sql(sql).pl()

    return ask, data_dir, database


@app.cell
def __(mo):
    mo.md("## The Tables")
    return


@app.cell
def __(duckdb, database, data_dir):
    import os

    # Delete old database and rebuild from scratch
    if database.exists():
        os.remove(database)

    with duckdb.connect(database) as _con:

        # ── PEOPLE ────────────────────────────────────────────────────────────
        _con.execute("""
            CREATE TABLE people (
                person_id   INTEGER PRIMARY KEY,
                first_name  VARCHAR NOT NULL,
                last_name   VARCHAR NOT NULL,
                work_email  VARCHAR NOT NULL UNIQUE,
                title       VARCHAR NOT NULL,
                start_date  DATE    NOT NULL,
                manager_id  INTEGER REFERENCES people(person_id)
            )
        """)

        # ── PROJECTS ──────────────────────────────────────────────────────────
        _con.execute("""
            CREATE TABLE projects (
                project_id  INTEGER PRIMARY KEY,
                name        VARCHAR NOT NULL,
                client_name VARCHAR,
                category    VARCHAR NOT NULL CHECK (category IN ('LLM app','data pipeline','internal tool')),
                budget      DECIMAL(12,2) NOT NULL CHECK (budget > 0),
                start_date  DATE    NOT NULL,
                status      VARCHAR NOT NULL CHECK (status IN ('planned','active','paused','done'))
            )
        """)

        # ── PROJECT_MEMBERS ───────────────────────────────────────────────────
        _con.execute("""
            CREATE TABLE project_members (
                person_id      INTEGER NOT NULL REFERENCES people(person_id),
                project_id     INTEGER NOT NULL REFERENCES projects(project_id),
                role           VARCHAR NOT NULL,
                hours_per_week INTEGER NOT NULL CHECK (hours_per_week >= 1 AND hours_per_week <= 40),
                joined_date    DATE    NOT NULL,
                PRIMARY KEY (person_id, project_id)
            )
        """)

        # ── TASKS ─────────────────────────────────────────────────────────────
        _con.execute("""
            CREATE TABLE tasks (
                task_id        INTEGER PRIMARY KEY,
                project_id     INTEGER NOT NULL REFERENCES projects(project_id),
                description    VARCHAR NOT NULL,
                created_date   DATE    NOT NULL,
                assigned_to    INTEGER REFERENCES people(person_id),
                due_date       DATE    NOT NULL,
                completed_date DATE,
                CHECK (completed_date IS NULL OR completed_date >= created_date)
            )
        """)

        # ── EXPENSES ──────────────────────────────────────────────────────────
        _con.execute("""
            CREATE TABLE expenses (
                expense_id   INTEGER PRIMARY KEY,
                project_id   INTEGER NOT NULL REFERENCES projects(project_id),
                expense_date DATE    NOT NULL,
                amount       DECIMAL(12,2) NOT NULL CHECK (amount > 0),
                category     VARCHAR NOT NULL CHECK (category IN ('GPU cloud','data labeling','software','travel')),
                note         VARCHAR
            )
        """)

        # ── VIEW: weekly_hours_by_person ──────────────────────────────────────
        # Business would check this every week to spot overloaded people
        _con.execute("""
            CREATE VIEW weekly_hours_by_person AS
            SELECT
                p.person_id,
                p.first_name || ' ' || p.last_name AS full_name,
                SUM(pm.hours_per_week) AS total_hours_per_week
            FROM people p
            JOIN project_members pm ON p.person_id = pm.person_id
            JOIN projects proj ON pm.project_id = proj.project_id
            WHERE proj.status = 'active'
            GROUP BY p.person_id, p.first_name, p.last_name
        """)

        # ── LOAD DATA ─────────────────────────────────────────────────────────
        # People must be loaded one row at a time (self-referential FK)
        import csv
        with open(data_dir / "people.csv") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Sort: managers (empty manager_id) first, then by manager_id
        def sort_key(r):
            return (0 if r["manager_id"] == "" else 1, r["manager_id"])
        rows.sort(key=sort_key)

        for r in rows:
            mgr = None if r["manager_id"] == "" else int(r["manager_id"])
            _con.execute(
                "INSERT INTO people VALUES (?, ?, ?, ?, ?, ?, ?)",
                [int(r["person_id"]), r["first_name"], r["last_name"],
                 r["work_email"], r["title"], r["start_date"], mgr]
            )

        # Load remaining tables from CSV
        for table in ["projects", "project_members", "tasks", "expenses"]:
            _con.execute(f"""
                COPY {table} FROM '{data_dir / f"{table}.csv"}' (HEADER TRUE)
            """)

    print("Database built successfully.")
    return


@app.cell
def __(mo):
    mo.md("## A Look at the Data")
    return


@app.cell
def __(ask):
    import polars as pl

    tasks_by_project = ask("""
        SELECT p.name AS project_name, COUNT(t.task_id) AS task_count
        FROM projects p
        LEFT JOIN tasks t ON p.project_id = t.project_id
        GROUP BY p.project_id, p.name
        ORDER BY task_count DESC
    """)
    tasks_by_project
    return pl, tasks_by_project


@app.cell
def __(ask, mo):
    # Chart: expenses by category
    expenses_by_cat = ask("""
        SELECT category, ROUND(SUM(amount), 2) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
    """)
    mo.md(f"""
    **Expense totals by category:**
    A real company would likely have GPU cloud as the dominant expense for an AI startup,
    which is what we see here. The distribution looks plausible.
    """)
    return (expenses_by_cat,)


@app.cell
def __(mo):
    mo.md("## Row Counts")
    return


@app.cell
def __(ask):
    ask("""
        SELECT 'people'          AS table_name, COUNT(*) AS row_count FROM people
        UNION ALL
        SELECT 'projects',        COUNT(*) FROM projects
        UNION ALL
        SELECT 'project_members', COUNT(*) FROM project_members
        UNION ALL
        SELECT 'tasks',           COUNT(*) FROM tasks
        UNION ALL
        SELECT 'expenses',        COUNT(*) FROM expenses
    """)
    return


@app.cell
def __(mo):
    mo.md("## A Row It Refuses")
    return


@app.cell
def __(database, duckdb):
    # Try to insert a row that breaks a constraint (budget <= 0)
    try:
        with duckdb.connect(database) as _con:
            _con.execute("""
                INSERT INTO projects VALUES (
                    99, 'Bad Project', NULL, 'LLM app', -500.00, '2026-01-01', 'active'
                )
            """)
        print("ERROR: Row was accepted but should have been rejected.")
    except Exception as e:
        print(f"Correctly refused: {e}")
    return


@app.cell
def __(mo):
    mo.md("## Answers You Already Knew")
    return


@app.cell
def __(ask):
    # 1. There should be 25 people
    ask("SELECT COUNT(*) AS people_count FROM people")
    return


@app.cell
def __(ask):
    # 2. Project 12 should have zero expenses (we intentionally gave it none)
    ask("""
        SELECT p.name, COUNT(e.expense_id) AS expense_count
        FROM projects p
        LEFT JOIN expenses e ON p.project_id = e.project_id
        WHERE p.project_id = 12
        GROUP BY p.name
    """)
    return


@app.cell
def __(ask):
    # 3. No task's completed_date should be before its created_date
    ask("""
        SELECT COUNT(*) AS violations
        FROM tasks
        WHERE completed_date < created_date
    """)
    return


@app.cell
def __(mo):
    mo.md("## The View")
    return


@app.cell
def __(ask):
    # weekly_hours_by_person view — people on active projects and their total weekly hours
    ask("SELECT * FROM weekly_hours_by_person ORDER BY total_hours_per_week DESC")
    return


if __name__ == "__main__":
    app.run()
