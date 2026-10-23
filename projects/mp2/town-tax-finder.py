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
    county = "Middlesex"
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    budget_dollars = 700000
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    tax_limit_dollars = 8000
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    fiscal_year = 2026
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


@app.cell
def _(requests):
    towns_requests = requests.get("https://oim.zhili.dev/ma/towns?county=Middlesex", timeout=10).json()
    towns_requests


    return (towns_requests,)


@app.cell
def _(towns_requests):
    door_codes = []
    for _town in towns_requests["items"]:
        door_codes.append(_town["dor_code"])

    door_codes
    return


@app.cell
def _(requests):
    town_history = requests.get("https://oim.zhili.dev/ma/towns/002/history", timeout=10).json()
    town_history["years"][0]["average_single_family_value_dollars"]
    return


@app.cell
def _(mo):

    import requests
    import csv

    county = "Middlesex"
    budget_dollars = 700000
    tax_limit_dollars = 8000
    fiscal_year = 2026

    BASE_URL = "https://oim.zhili.dev/ma"


    def get_county_towns(county):
        towns = []
        page = 1

        while True:
            response = requests.get(
                f"{BASE_URL}/towns",
                params={
                    "county": county,
                    "page": page,
                    "per_page": 100
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            page_towns = data.get("items", [])

            if not page_towns:
                break

            towns.extend(page_towns)
            page += 1

        return towns


    def get_town_financials(towns, fiscal_year):
        financial_records = []

        for town in towns:
            dor_code = town["dor_code"]

            response = requests.get(
                f"{BASE_URL}/towns/{dor_code}/history",
                timeout=10
            )
            response.raise_for_status()
            history = response.json()

            for year_data in history.get("years", []):
                if year_data["fiscal_year"] == fiscal_year:
                    record = {
                        "name": town["name"],
                        "county": county,
                        "dor_code": dor_code,
                        "fiscal_year": fiscal_year,
                        "residential_rate_per_thousand":
                            year_data["residential_rate_per_thousand"],
                        "average_single_family_value_dollars":
                            year_data["average_single_family_value_dollars"],
                        "average_single_family_bill_dollars":
                            year_data["average_single_family_bill_dollars"]
                    }

                    financial_records.append(record)
                    break

        return financial_records


    towns = get_county_towns(county)
    ma_towns = get_town_financials(towns, fiscal_year)

    print(f"Number of towns retrieved: {len(towns)}")
    print(f"Towns with data for {fiscal_year}: {len(ma_towns)}")


    all_town_costs = {
        town["name"].lower(): [
            town["average_single_family_value_dollars"],
            town["average_single_family_bill_dollars"]
        ]
        for town in ma_towns
    }

    print(all_town_costs)


    qualifying_towns = {
        town["name"].lower(): [
            town["average_single_family_value_dollars"],
            town["average_single_family_bill_dollars"]
        ]
        for town in ma_towns
        if town["average_single_family_value_dollars"] <= budget_dollars
        and town["average_single_family_bill_dollars"] < tax_limit_dollars
    }

    qualifying_towns = dict(
        sorted(
            qualifying_towns.items(),
            key=lambda item: item[1][1]
        )
    )

    print("Towns that meet both requirements:")
    print(qualifying_towns)


    csv_columns = [
        "name",
        "county",
        "dor_code",
        "fiscal_year",
        "residential_rate_per_thousand",
        "average_single_family_value_dollars",
        "average_single_family_bill_dollars"
    ]

    ma_towns_csv = (
        mo.notebook_dir().parent / "data" / "ma-towns.csv"
    )

    ma_towns_csv.parent.mkdir(parents=True, exist_ok=True)

    with open(ma_towns_csv, "w", newline="", encoding="utf-8") as _file:
        writer = csv.DictWriter(
            _file,
            fieldnames=csv_columns,
            extrasaction="ignore"
        )
        writer.writeheader()
        writer.writerows(ma_towns)

    print(f"CSV saved to: {ma_towns_csv}")

    return (
        BASE_URL,
        budget_dollars,
        county,
        fiscal_year,
        ma_towns,
        qualifying_towns,
        requests,
        tax_limit_dollars,
        towns,
    )


@app.cell
def _(county, fiscal_year, ma_towns, towns):
    # Calculate the property tax bill as a percentage of income per capita

    financial_data = {
        town["dor_code"]: town
        for town in ma_towns
    }

    income_tax_results = []

    for town in towns:
        dor_code = town["dor_code"]

        # Skip towns without financial data for the selected fiscal year
        if dor_code not in financial_data:
            continue

        income_value = town["income_per_capita_dollars"]
        town_tax_bill = financial_data[dor_code][
            "average_single_family_bill_dollars"
        ]

        # Calculate tax bill as a percentage of income per capita
        if income_value is not None and income_value > 0:
            tax_percentage = (town_tax_bill / income_value) * 100
        else:
            tax_percentage = None

        income_tax_results.append({
            "name": town["name"],
            "income_per_capita_dollars": income_value,
            "average_single_family_bill_dollars": town_tax_bill,
            "tax_percentage": tax_percentage
        })

    # Sort towns from lowest to highest percentage
    income_tax_results.sort(
        key=lambda town: (
            town["tax_percentage"] is None,
            town["tax_percentage"] if town["tax_percentage"] is not None else 0
        )
    )

    # Print the results
    print(f"Property Tax Bill as a Percentage of Income: {county} County")
    print(f"Fiscal year: {fiscal_year}\n")

    print(
        f"{'Town':<22}"
        f"{'Income Per Capita':>22}"
        f"{'Average Tax Bill':>20}"
        f"{'Bill / Income':>16}"
    )
    print("-" * 80)

    for town in income_tax_results:
        income_value = town["income_per_capita_dollars"]
        town_tax_bill = town["average_single_family_bill_dollars"]
        tax_percentage = town["tax_percentage"]

        income_text = (
            f"${income_value:,.0f}"
            if income_value is not None
            else "N/A"
        )

        bill_text = (
            f"${town_tax_bill:,.2f}"
            if town_tax_bill is not None
            else "N/A"
        )

        percentage_text = (
            f"{tax_percentage:.2f}%"
            if tax_percentage is not None
            else "N/A"
        )

        print(
            f"{town['name']:<22}"
            f"{income_text:>22}"
            f"{bill_text:>20}"
            f"{percentage_text:>16}"
        )

    print("-" * 80)
    print(f"Total towns displayed: {len(income_tax_results)}")
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


@app.cell
def _(
    budget_dollars,
    county,
    fiscal_year,
    qualifying_towns,
    tax_limit_dollars,
):


    print(f"\nTowns in {county} County that meet both requirements")
    print(f"Fiscal year: {fiscal_year}")
    print()

    print(
        f"{'Town':<20}"
        f"{'Average Home Value':>22}"
        f"{'Residential Tax Bill':>24}"
    )

    print("-" * 66)

    for town_name, costs in qualifying_towns.items():
        home_value = costs[0]
        tax_bill = costs[1]

        print(
            f"{town_name.title():<20}"
            f"${home_value:>20,.0f}"
            f"${tax_bill:>22,.2f}"
        )

    print("-" * 66)

    number_of_towns = len(qualifying_towns)

    if number_of_towns > 0:
        cheapest_town = next(iter(qualifying_towns))
        cheapest_costs = qualifying_towns[cheapest_town]

        cheapest_bill = cheapest_costs[1]
        cheapest_home_value = cheapest_costs[0]

        print(
            f"\nFor a budget of ${budget_dollars:,.0f} and an annual "
            f"property tax limit of ${tax_limit_dollars:,.0f}, "
            f"{number_of_towns} towns in {county} County meet both "
            f"requirements for fiscal year {fiscal_year}. "
            f"The lowest average tax bill is in {cheapest_town.title()}, "
            f"at ${cheapest_bill:,.2f} per year, with an average "
            f"single-family home value of ${cheapest_home_value:,.0f}."
        )
    else:
        print(
            f"\nNo towns in {county} County meet both the "
            f"${budget_dollars:,.0f} home budget and the "
            f"${tax_limit_dollars:,.0f} annual property tax limit "
            f"for fiscal year {fiscal_year}."
        )

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


@app.cell
def _(BASE_URL, county, requests, towns):
    response = requests.get(
        f"{BASE_URL}/towns",
        params={"county": county, "page": 1, "per_page": 100},
        timeout=10
    )
    response.raise_for_status()
    data = response.json()

    reported_total = data["pagination"]["total"]
    collected_total = len(towns)

    print(f"Town count reported by API: {reported_total}")
    print(f"Town count collected by code: {collected_total}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Like I said in my explanation and plan for this section I am comparing the count of towns from the api with the length of town before going through the towns so then I compare the length of the what I have used and edited through to get information as well the total of towns beofre sifting through them all
    """)
    return


@app.cell
def _(requests):
    def _():
        town_history = requests.get(
            "https://oim.zhili.dev/ma/towns/002/history",
            timeout=10
        ).json()

        for year in town_history["years"]:
            if year["fiscal_year"] == 2026:
                average_home_value = year["average_single_family_value_dollars"]
                average_tax_bill = year["average_single_family_bill_dollars"]

                print(f"Average single-family home value: ${average_home_value:,.2f}")
        return print(f"Average single-family tax bill: ${average_tax_bill:,.2f}")
    


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    {
      "dor_code": "002",
      "name": "Acton",
      "years": [
        {
          "fiscal_year": 2026,
          "residential_rate_per_thousand": 16.23,
          "commercial_rate_per_thousand": 16.23,
          "single_family_parcels": 5011,
          "average_single_family_value_dollars": 937779,
          "average_single_family_bill_dollars": 15220
        }
      ]
    }
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As a second test I went straight to the source and looked up this sepcific town and compared it to what was being called from the api so I have good reason to belive that since the numbers matched in this case other cases have no reason not to match
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
    I used an ai agent to loop through the towns in Middlesex County andto do so by year so a loop within a loop and I thought it was entirely possible to miss a section or miss a town so I compared the raw list of towns in Middlesex County tothe final amount of towns the program went through to make sureevery town was accounted for and nothing was skipped during the nested loop process.
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
    The function get_town_financials() was particularly difficult and for diferent parts of the code I used the agent to fix my grammar and to fix how I was going about solving a problem so I would start and then run into issues the agent would clean up or fix a lot of the errors that were coming up or to help me achieve the same result or a better reuslt in a better way. The function get_town_financials() in particular was difficult. The function passes the list of towns from another function and the fiscal year requirement from the question variables it goes through each town and get the financials for the designated year 2026. There is a loop that is going through every towns financial records for every year until the year matches 2026 and then appending it to records  so their is a final list of different towns financials so that they can then be passed on to see whether they fit other criteria for the specific family about their budget
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
    Right before section 5, I calculated the tax bill as a percentage of income for every town in Middlesex County. It was difficult, and I had to reuse code from other sections as well get some aid from ai with some errors that kept occurring. It is interesting to see which towns have a higher income or tax bill as percentages like the first entry sherborn has about 5% whereas in Everett the average tax bill is 22% of average income per capita almost a 5x increase but most town seem to hover around the 13-18% range for tax bill as a percentage of income, suggesting that while there are outliers on both ends of the spectrum, the majority of towns in Middlesex County face a fairly similar tax burden relative to their income levels.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    5-6 hours
    """)
    return


if __name__ == "__main__":
    app.run()
