import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Prediction
    ###Question 6

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


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
