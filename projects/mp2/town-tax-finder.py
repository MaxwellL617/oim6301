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
    1.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Question. Who would use this, and what decision does it help them make? Two or three sentences, in words somebody outside this course would understand.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If this did not exists and I wanted to move to a town and purchase a home I would have to go to a variety of sites and do a variety of searches and deal with different UI's which ight not always be complimentary or easy to use. With a tool in python that can directly get() the data from a source and manipulate it, that is extremely valuable. Being able to compare prices of different towns and counties directly to a budget quickly is incredibly useful. Another usecase is for elected officials to find out where there are outliers in towns and income or why some towns have a high value or low value and how they can innact public policy to tr to reinvigorate towns with low income per capita or lower home prices. A tool where you can search town by town data of home prices, income, town finances, and other town related data it can make it easier to sort through essential information or inofrmation you need instead of having to manually browse through multiple town websites, government portals, and real estate listings that each have their own format and structure.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    2.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    My Plan Before AI. Before you ask your agent anything, open the API's address in your browser and read what comes back. Then write how you would solve it: the steps, in order, in plain words, in five lines or more. Then answer these:

    Which functions will your tool need? For each, what goes in and what comes out?
    Which addresses will they request?
    How will you know you have every record?
    Which check will you use in section 6, and which two numbers should agree?
    Commit with the message mp2: plan before AI.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    county = "Middlesex"
    budget_dollars = 700000
    tax_limit_dollars = 8000
    fiscal_year = 2026

     "dor_code": "string",
      "name": "string",
      "years": [
        {
          "fiscal_year": 0,
          "residential_rate_per_thousand": 10.17,
          "commercial_rate_per_thousand": 0,
          "single_family_parcels": 0,
          "average_single_family_value_dollars": 0,
          "average_single_family_bill_dollars": 0
        }
      ]

    The above are the parameters for this couple to find a house, along with an example in JSON of how the data is organized. The numbers we are lookingfor in this particular question are the average_single_family_value_dollars, which is the average home value in a town, and commercial_rate_per_thousand, which states the tax rate per $1000 of value as well as average_single_family_bill_dollars, which states the average bill in taxes each family has to pay. So I am going to create a definition that will pass each requirement and substitute each on as a query to get a list of dictionaries or lists that correspond to the towns and their values.

    The issue is finding the towns that meet the criteria but first I think that requires going through all the towns. Which might mean calling all of the towns and appending them to a list or a list of dictionaries. If not that then just looping through all the towns with the api and categorizing them base don the value and a set of OR statements like if the average home price is over 700,000 then it is automatically disqualified, or if the calcuated tax on the home would be more than 8000 that would also be disqualified which should leave me with a list of towns and values that pass the test, which i can then manually make into a data frame or save as a csv and then call alter using methods from workbook 5.

    I will need a function that will search through the api and the values and pass my requirements into the function and I may also need a function that works to append those values to a list but I think I might be able to do both at once. I might need severl functions to pass each requirement but I think I should be able to pass several variables into one function.

    To check I have every record i can do a count on a list with all the appended towns and their information and then to another count function in the api to find hwo many towns were there to start with and if that number does not match then i have done smething wrong. My list should include all towns regardless of criteria and then with another function, start aggregating through the list and then I can compare the first list to the total numer of entries through the api. The numbers that should agree are the total amount of entries I have and the total amount of entries that are on the api
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    3.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Inputs. Every input in one cell.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    4.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Work. Your functions, and the code that uses them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    5.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Answer. Your result table, printed with print and f-strings with the columns lined up, and one sentence that answers the question in section 1 with the numbers in it. Print the sentence from code with an f-string, so that it changes when the data does.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    6.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    How I Know These Numbers Are Right. Reach at least one result a second way, in this notebook, and show that the two agree. Write a cell that gets the same number from other fields, or open the raw reply in your browser and find each number of one row of your table there. For instance: an average bill is close to the average value times the tax rate divided by 1,000; an order's total equals the sum of its lines; the number of records you collected equals the total the API reports. At least one of those checks runs as code, and shows both numbers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    7.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Working With the Agent. Pick one piece of AI output you did not accept as-is. What did it give you, what did you change, and how did you know? Point to the commit or the cell. If the agent got it right the first time: What did you do to verify that? Pointing to your check in section 6 is enough.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    8.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Reading It Back. Pick two functions in your notebook that your agent wrote or helped write. For each, write in your own words what goes in, what comes out, and one line you had to ask about. Then choose one change to what the tool does, such as another county, another week or another rule. Changing one value in your Inputs cell is enough. Write what you expect to change in the answer. Commit with the message mp2: prediction, make the change, run it, and write what happened and whether it matched.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    9.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Going Further. What you tried past the main task, what you found, and where it is in the notebook.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    10.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Time Spent. About how many hours this project took you outside class, as one number. It is not graded.
    """)
    return


if __name__ == "__main__":
    app.run()
