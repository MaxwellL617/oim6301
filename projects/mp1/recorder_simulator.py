# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///
"""Mini Project 1.
"""

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", sql_output="polars")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Mini Project 1

    Your choice of option, what each one asks for, the due date and how it is graded are on the Mini Project 1 page of the course site, linked from the calendar. This notebook is the shape to build it in. Keep the headings, and replace each line in italics with your own.

    Save it in your course repository as `projects/mp1/<your-tool>.py`, named for what it does, such as `loan-schedule.py`, and open it with `uv run marimo edit`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. The Question

    *Who would use this, and what decision does it help them make? Two or three sentences, in words somebody outside this course would understand.*
    """)
    return


@app.cell
def _():
    #This is for someone to help simulate their demand schedule and lead time for orders and reorders and how you might simulate demand. For a company that depends on daily demand and the price of stocking items for every additional day having an idea of how much inventory you might need at any given time and what you shoudl expect from not only demand scheduling but exactly how much you should use.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. My Plan Before AI

    *Before you ask your agent anything, write how you would solve it: the steps, in order, in plain words, in five lines or more. Then answer these two questions:*

    - *What does your loop carry from one step to the next, the way a running total carries its sum?*
    - *Which check will you use in section 6, and which two numbers should agree?*

    *Commit this notebook with the message `mp1: plan before AI`.*
    """)
    return


@app.cell
def _():
    #My plan is to have a rough draft and write it fully on my own without the use of ai to get an idea of the problem at hand and exactly what I need to do. I will use a loop to simulate the days based on the length of the list of daily demand. The demand length is 30 so it will run for 30 loops in a for loop I am going to try to hold onto variables and update them through every iteration which requires creating variables outside of the loop and setting them back to 0 at the end of the loop while also appending values after they have gone through change or a formula so that at the end i can actually see the set demand and stock keeping schedule

    #plan
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Inputs

    Every number the project starts from goes in the cell below, and nowhere else, so that changing one input changes every result after it.

    Copy in the default inputs for your option from the Mini Project 1 page. If you chose D, your own option, type your data in here, or ask your agent to generate it with `faker`. The required part reads no file.
    """)
    return


@app.cell
def _():
    def _():
        starting_stock = 60
        order_quantity = 100
        lead_time_days = 3
        reorder_points = [20, 30, 40, 50]
        daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,
                        9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]

    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. The Work

    Add as many cells as you need. Try each step yourself before you ask your agent, and commit as you go.
    """)
    return


@app.cell
def _():
    starting_stock = 60
    order_quantity = 100
    lead_time_days = 3
    reorder_points = [20, 30, 40, 50]
    daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,
                    9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]

    avg_20 = []
    avg_30 = []
    avg_40 = []
    avg_50 = []

    lists = [avg_20, avg_30, avg_40, avg_50]

    order_amount = 0
    added_stock = 0
    lost_units = 0
    arrived_stock = 0
    wait_arrived = 0


    lead_a = 0
    lead_b = 0
    lead_c = 0

    def lead_calc():
        global starting_stock
        global order_amount
        global total_cost
        starting_stock += 100
        order_amount += 100
        total_cost += 8



    for z in range(len(reorder_points)):
        print (f"For reorder point: {reorder_points[z]}")
        print("Day", " "*5,"Starting Stock"," "*5,"Arrived", " "*5, "Demand"," "*5,"Sold"," "*5,"Lost"," "*5,"Ending Stock", " "*5, "Units Ordered")
        starting_stock = 60
        total_cost = 0
        for i in range(len(daily_demand)):
            print(i+1, " "*10,starting_stock, " "*15,arrived_stock," "*10, daily_demand[i]," "*10,daily_demand[i]," "*5,lost_units, " "*10,starting_stock-daily_demand[i]," "*15, order_amount )
            starting_stock -= daily_demand[i]
            order_amount = 0
            added_stock = 0
            arrived_stock = 0
    
            if starting_stock <= reorder_points[z]:
                lead_a +=1
                if lead_a == 3:
                    lead_calc()
                    lead_a = 0
                    added_stock +=100
            
                if lead_a > 0:
                    lead_b +=1
                if lead_b == 3:
                    lead_calc()
                    lead_b = 0
                    added_stock +=100
        
                if lead_a > 0 and lead_b > 0:
                    lead_c += 1
                if lead_c > 0:
                    lead_c += 1
                if lead_c == 3:
                    lead_calc()
                    lead_c = 0
                    added_stock +=100
        
                if added_stock == 100:
                    wait_arrived += 1
                if wait_arrived == 3:
                    arrived_stock = 100
                    if added_stock == 200:
                        arrived_stock = 200       
            
            if starting_stock < 0:
                units_lost = abs(starting_stock)
                starting_stock = 0
            total_cost += starting_stock * .5
        
            lists[z].append(starting_stock)

    result1 = sum(avg_20)/len(avg_20)
    print(f"The average starting stock when the redorder point is 20 is: {result1}" )
    result2 = sum(avg_30)/len(avg_30)
    print(f"The average starting stock when the redorder point is 30 is: {result2}" )
    result3 = sum(avg_40)/len(avg_40)
    print(f"The average starting stock when the redorder point is 40 is: {result3}" )
    result4 = sum(avg_50)/len(avg_50)
    print(f"The average starting stock when the redorder point is 50 is: {result4}" )
    return


@app.cell
def _():
    def _():
        starting_stock = 60
        order_quantity = 100
        lead_time_days = 3
        reorder_points = [20, 30, 40, 50]
        daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,
                        9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]

        avg_20 = []
        avg_30 = []
        avg_40 = []
        avg_50 = []
        lists = [avg_20, avg_30, avg_40, avg_50]

        for z in range(len(reorder_points)):
            starting_stock = 60
            print(f"For reorder point: {reorder_points[z]}")
            print("Day", " "*5, "Starting Stock", " "*5, "Arrived", " "*5,
                  "Demand", " "*5, "Sold", " "*5, "Lost", " "*5,
                  "Ending Stock", " "*5, "Units Ordered")

        
            total_cost = 0
            order_pending = False
            days_since_order = 0

            for i in range(len(daily_demand)):
                arrived_today = 0
                units_ordered_today = 0
                lost_today = 0
                sold_today = daily_demand[i]

                print(i + 1, " "*10, starting_stock, " "*15, arrived_today, " "*10,
                      daily_demand[i], " "*10, sold_today, " "*5, lost_today, " "*10,
                      starting_stock, " "*15, units_ordered_today)

                if order_pending:
                    days_since_order += 1
                    if days_since_order == lead_time_days:
                        starting_stock += order_quantity
                        arrived_today = order_quantity
                        order_pending = False
                        days_since_order = 0

            
                if sold_today > starting_stock:
                    lost_today = sold_today - starting_stock
                    sold_today = starting_stock
                starting_stock -= sold_today

                if starting_stock <= reorder_points[z] and not order_pending:
                    order_pending = True
                    days_since_order = 0
                    units_ordered_today = order_quantity

                total_cost += starting_stock * 0.5

            
                lists[z].append(starting_stock)

        result1 = sum(avg_20) / len(avg_20)
        print(f"The average starting stock when the reorder point is 20 is: {result1}")
        result2 = sum(avg_30) / len(avg_30)
        print(f"The average starting stock when the reorder point is 30 is: {result2}")
        result3 = sum(avg_40) / len(avg_40)
        print(f"The average starting stock when the reorder point is 40 is: {result3}")
        result4 = sum(avg_50) / len(avg_50)
        return print(f"The average starting stock when the reorder point is 40 is: {result4}")


    _()
    return


@app.cell
def _():
    def _():
        starting_stock = 60
        order_quantity = 100
        lead_time_days = 3
        reorder_points = [20, 30, 40, 50]
        daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,
                        9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]

        avg_20 = []
        avg_30 = []
        avg_40 = []
        avg_50 = []
        lists = [avg_20, avg_30, avg_40, avg_50]

        lost_20 = []
        lost_30 = []
        lost_40 = []
        lost_50 = []
        lost_lists = [lost_20, lost_30, lost_40, lost_50]

        for z in range(len(reorder_points)):
            print(f"For reorder point: {reorder_points[z]}")
            print("Day", " "*5, "Starting Stock", " "*5, "Arrived", " "*5,
                  "Demand", " "*5, "Sold", " "*5, "Lost", " "*5,
                  "Ending Stock", " "*5, "Units Ordered")

            starting_stock = 60
            total_cost = 0
            order_pending = False
            days_since_order = 0

            for i in range(len(daily_demand)):
                arrived_today = 0
                units_ordered_today = 0
                lost_today = 0

                if order_pending:
                    days_since_order += 1
                    if days_since_order == lead_time_days:
                        starting_stock += order_quantity
                        arrived_today = order_quantity
                        order_pending = False
                        days_since_order = 0

                sold_today = daily_demand[i]
                if sold_today > starting_stock:
                    lost_today = sold_today - starting_stock
                    sold_today = starting_stock
                starting_stock -= sold_today

                if starting_stock <= reorder_points[z] and not order_pending:
                    order_pending = True
                    days_since_order = 0
                    units_ordered_today = order_quantity

                total_cost += starting_stock * 0.5

                print(i + 1, " "*10, starting_stock, " "*15, arrived_today, " "*10,
                      daily_demand[i], " "*10, sold_today, " "*5, lost_today, " "*10,
                      starting_stock, " "*15, units_ordered_today)

                lists[z].append(starting_stock)
                lost_lists[z].append(lost_today)

        result1 = sum(avg_20) / len(avg_20)
        print(f"The average starting stock when the reorder point is 20 is: {result1}")
        result2 = sum(avg_30) / len(avg_30)
        print(f"The average starting stock when the reorder point is 30 is: {result2}")
        result3 = sum(avg_40) / len(avg_40)
        print(f"The average starting stock when the reorder point is 40 is: {result3}")
        result4 = sum(avg_50) / len(avg_50)
        print(f"The average starting stock when the reorder point is 50 is: {result4}")

        lost_result1 = sum(lost_20) 
        print(f"The total lost units per day when the reorder point is 20 is: {lost_result1}")
        lost_result2 = sum(lost_30) 
        print(f"The total lost units per day when the reorder point is 30 is: {lost_result2}")
        lost_result3 = sum(lost_40) 
        print(f"The total lost units per day when the reorder point is 40 is: {lost_result3}")
        lost_result4 = sum(lost_50) 
        return print(f"The total lost units per day when the reorder point is 50 is: {lost_result4}")


    _()
    return


@app.cell
def _():
    def _():
        starting_stock = 60
        order_quantity = 100
        lead_time_days = 3
        reorder_points = [20, 25, 30, 35, 40, 50]
        daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]

        avg_20 = []
        avg_25 = []
        avg_30 = []
        avg_35 = []
        avg_40 = []
        avg_50 = []
        lists = [avg_20, avg_25, avg_30, avg_35, avg_40, avg_50]

        lost_20 = []
        lost_25 = []
        lost_30 = []
        lost_35 = []
        lost_40 = []
        lost_50 = []
        lost_lists = [lost_20, lost_25, lost_30, lost_35, lost_40, lost_50]

        for z in range(len(reorder_points)):
            print(f"For reorder point: {reorder_points[z]}")
            print("Day", " "*5, "Starting Stock", " "*5, "Arrived", " "*5,
                  "Demand", " "*5, "Sold", " "*5, "Lost", " "*5,
                  "Ending Stock", " "*5, "Units Ordered")

            starting_stock = 60
            total_cost = 0
            order_pending = False
            days_since_order = 0
            deliveries = 0

            for i in range(len(daily_demand)):
                day_start_stock = starting_stock  # stock on hand before today's events
                arrived_today = 0
                units_ordered_today = 0
                lost_today = 0
                sold_today = daily_demand[i]

                if order_pending:
                    days_since_order += 1
                    if days_since_order == lead_time_days:
                        starting_stock += order_quantity
                        arrived_today = order_quantity
                        order_pending = False
                        days_since_order = 0

                if sold_today > starting_stock:
                    lost_today = sold_today - starting_stock
                    sold_today = starting_stock
                starting_stock -= sold_today

                if starting_stock <= reorder_points[z] and not order_pending:
                    order_pending = True
                    days_since_order = 0
                    units_ordered_today = order_quantity

                total_cost += starting_stock * 0.5

                # print after everything for the day has happened
                print(i + 1, " "*10, day_start_stock, " "*15, arrived_today, " "*10,
                      daily_demand[i], " "*10, sold_today, " "*5, lost_today, " "*10,
                      starting_stock, " "*15, units_ordered_today)

                lists[z].append(starting_stock)
                lost_lists[z].append(lost_today)

        

        result1 = sum(avg_20) / len(avg_20)
        print(f"The average starting stock when the reorder point is 20 is: {result1}")
        result2 = sum(avg_30) / len(avg_30)
        print(f"The average starting stock when the reorder point is 30 is: {result2}")
        result3 = sum(avg_40) / len(avg_40)
        print(f"The average starting stock when the reorder point is 40 is: {result3}")
        result4 = sum(avg_50) / len(avg_50)
        print(f"The average starting stock when the reorder point is 50 is: {result4}")
        result5 = sum(avg_25) / len(avg_25)
        print(f"The average starting stock when the reorder point is 25 is: {result5}")
        result6 = sum(avg_35) / len(avg_35)
        print(f"The average starting stock when the reorder point is 35 is: {result6}")

        lost_result1 = sum(lost_20)
        print(f"The total lost units per day when the reorder point is 20 is: {lost_result1}")
        lost_result5 = sum(lost_25)
        print(f"The total lost units per day when the reorder point is 25 is: {lost_result5}")
        lost_result6 = sum(lost_35)
        print(f"The total lost units per day when the reorder point is 35 is: {lost_result6}")
        lost_result2 = sum(lost_30)
        print(f"The total lost units per day when the reorder point is 30 is: {lost_result2}")
        lost_result3 = sum(lost_40)
        print(f"The total lost units per day when the reorder point is 40 is: {lost_result3}")
        lost_result4 = sum(lost_50)
        return print(f"The total lost units per day when the reorder point is 50 is: {lost_result4}")

    
   


    _()
    return


@app.cell
def _():
    def _():
        starting_stock = 60
        order_quantity = 100
        lead_time_days = 3
        reorder_points = [20, 25, 30, 35, 40, 50]
        daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]

        avg_20 = []
        avg_25 = []
        avg_30 = []
        avg_35 = []
        avg_40 = []
        avg_50 = []
        lists = [avg_20, avg_25, avg_30, avg_35, avg_40, avg_50]

        lost_20 = []
        lost_25 = []
        lost_30 = []
        lost_35 = []
        lost_40 = []
        lost_50 = []
        lost_lists = [lost_20, lost_25, lost_30, lost_35, lost_40, lost_50]

        for z in range(len(reorder_points)):
            print(f"For reorder point: {reorder_points[z]}")
            print("Day", " "*5, "Starting Stock", " "*5, "Arrived", " "*5,
                  "Demand", " "*5, "Sold", " "*5, "Lost", " "*5,
                  "Ending Stock", " "*5, "Units Ordered")

            starting_stock = 60
            total_cost = 0
            order_pending = False
            days_since_order = 0
            deliveries = 0  # running total of units that actually arrived
            total_sold = 0  # running total of units actually sold

            for i in range(len(daily_demand)):
                day_start_stock = starting_stock  # stock on hand before today's events
                arrived_today = 0
                units_ordered_today = 0
                lost_today = 0
                sold_today = daily_demand[i]

                if order_pending:
                    days_since_order += 1
                    if days_since_order == lead_time_days:
                        starting_stock += order_quantity
                        arrived_today = order_quantity
                        deliveries += order_quantity
                        order_pending = False
                        days_since_order = 0

                if sold_today > starting_stock:
                    lost_today = sold_today - starting_stock
                    sold_today = starting_stock
                starting_stock -= sold_today
                total_sold += sold_today

                if starting_stock <= reorder_points[z] and not order_pending:
                    order_pending = True
                    days_since_order = 0
                    units_ordered_today = order_quantity

                total_cost += starting_stock * 0.5

                # print after everything for the day has happened
                print(i + 1, " "*10, day_start_stock, " "*15, arrived_today, " "*10,
                      daily_demand[i], " "*10, sold_today, " "*5, lost_today, " "*10,
                      starting_stock, " "*15, units_ordered_today)

                lists[z].append(starting_stock)
                lost_lists[z].append(lost_today)

            independent_check = 60 + deliveries - total_sold
            print(f"The independent check for reorder point is : {independent_check}")

        result1 = sum(avg_20) / len(avg_20)
        print(f"The average starting stock when the reorder point is 20 is: {result1}")
        result2 = sum(avg_30) / len(avg_30)
        print(f"The average starting stock when the reorder point is 30 is: {result2}")
        result3 = sum(avg_40) / len(avg_40)
        print(f"The average starting stock when the reorder point is 40 is: {result3}")
        result4 = sum(avg_50) / len(avg_50)
        print(f"The average starting stock when the reorder point is 50 is: {result4}")
        result5 = sum(avg_25) / len(avg_25)
        print(f"The average starting stock when the reorder point is 25 is: {result5}")
        result6 = sum(avg_35) / len(avg_35)
        print(f"The average starting stock when the reorder point is 35 is: {result6}")

        lost_result1 = sum(lost_20)
        print(f"The total lost units per day when the reorder point is 20 is: {lost_result1}")
        lost_result5 = sum(lost_25)
        print(f"The total lost units per day when the reorder point is 25 is: {lost_result5}")
        lost_result6 = sum(lost_35)
        print(f"The total lost units per day when the reorder point is 35 is: {lost_result6}")
        lost_result2 = sum(lost_30)
        print(f"The total lost units per day when the reorder point is 30 is: {lost_result2}")
        lost_result3 = sum(lost_40)
        print(f"The total lost units per day when the reorder point is 40 is: {lost_result3}")
        lost_result4 = sum(lost_50)
        return print(f"The total lost units per day when the reorder point is 50 is: {lost_result4}")


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. The Answer

    *A table of your results in the cell below, printed with `print` and f-strings, then one sentence here that answers the question in section 1, with the number in it.*
    """)
    return


@app.cell
def _():
    def _():
        starting_stock = 60
        order_quantity = 100
        lead_time_days = 3
        reorder_points = [20, 25, 30, 35, 40, 50]
        daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,
                        9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]

        results = []  

        for z in range(len(reorder_points)):
            stock_list = []
            lost_list = []
            days_with_lost = 0
            reorder_count = 0

            starting_stock = 60
            order_pending = False
            days_since_order = 0

            for i in range(len(daily_demand)):
                if order_pending:
                    days_since_order += 1
                    if days_since_order == lead_time_days:
                        starting_stock += order_quantity
                        order_pending = False
                        days_since_order = 0

                sold_today = daily_demand[i]
                lost_today = 0
                if sold_today > starting_stock:
                    lost_today = sold_today - starting_stock
                    sold_today = starting_stock
                starting_stock -= sold_today

                if lost_today > 0:
                    days_with_lost += 1

                if starting_stock <= reorder_points[z] and not order_pending:
                    order_pending = True
                    days_since_order = 0
                    reorder_count += 1

                stock_list.append(starting_stock)
                lost_list.append(lost_today)

            record = {
                "reorder_point": reorder_points[z],
                "avg_stock": sum(stock_list) / len(stock_list),
                "total_lost": sum(lost_list),
                "days_with_lost": days_with_lost,
                "reorder_count": reorder_count,
            }
            results.append(record)

        print("Reorder Point", " "*5, "Avg Starting Stock", " "*5, "Total Lost Units",
              " "*5, "Days With Lost Units", " "*5, "Number of Reorders")
        for record in results:
            print(record["reorder_point"], " "*15, round(record["avg_stock"], 1),
                  " "*25, record["total_lost"], " "*20, record["days_with_lost"],
                  " "*25, record["reorder_count"])


    _()
    return


@app.cell
def _():
    #The best reorder point is 40. With an average starting stock of 48.4, total units lost being 0, days with lost units also being 0, and the number of reorder points being the same amount as every other reorder point 40 is clearly the best. With 48.4 as the average starting stock that is plenty for safetly stock while also not being too much where t would cost more for every additional unit. The reorder point of 40 aslo has no units lost and no days of lost units so the reorder point of 40 is definitely the ideal and the recommendation. 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. How I Know These Numbers Are Right

    *At least one check that reaches a result a second, independent way. Name what you compared and what came out.*
    """)
    return


@app.cell
def _():
    def _():
        starting_stock = 60
        order_quantity = 100
        lead_time_days = 3
        reorder_points = [20, 25, 30, 35, 40, 50]
        daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]

        avg_20 = []
        avg_25 = []
        avg_30 = []
        avg_35 = []
        avg_40 = []
        avg_50 = []
        lists = [avg_20, avg_25, avg_30, avg_35, avg_40, avg_50]

        lost_20 = []
        lost_25 = []
        lost_30 = []
        lost_35 = []
        lost_40 = []
        lost_50 = []
        lost_lists = [lost_20, lost_25, lost_30, lost_35, lost_40, lost_50]

        for z in range(len(reorder_points)):
            print(f"For reorder point: {reorder_points[z]}")
            print("Day", " "*5, "Starting Stock", " "*5, "Arrived", " "*5,
                  "Demand", " "*5, "Sold", " "*5, "Lost", " "*5,
                  "Ending Stock", " "*5, "Units Ordered")

            starting_stock = 60
            total_cost = 0
            order_pending = False
            days_since_order = 0
            deliveries = 0  # running total of units that actually arrived
            total_sold = 0  # running total of units actually sold

            for i in range(len(daily_demand)):
                day_start_stock = starting_stock  # stock on hand before today's events
                arrived_today = 0
                units_ordered_today = 0
                lost_today = 0
                sold_today = daily_demand[i]

                if order_pending:
                    days_since_order += 1
                    if days_since_order == lead_time_days:
                        starting_stock += order_quantity
                        arrived_today = order_quantity
                        deliveries += order_quantity
                        order_pending = False
                        days_since_order = 0

                if sold_today > starting_stock:
                    lost_today = sold_today - starting_stock
                    sold_today = starting_stock
                starting_stock -= sold_today
                total_sold += sold_today

                if starting_stock <= reorder_points[z] and not order_pending:
                    order_pending = True
                    days_since_order = 0
                    units_ordered_today = order_quantity

                total_cost += starting_stock * 0.5

                # print after everything for the day has happened
                print(i + 1, " "*10, day_start_stock, " "*15, arrived_today, " "*10,
                      daily_demand[i], " "*10, sold_today, " "*5, lost_today, " "*10,
                      starting_stock, " "*15, units_ordered_today)

                lists[z].append(starting_stock)
                lost_lists[z].append(lost_today)

            independent_check = 60 + deliveries - total_sold
            print(f"The independent check for reorder point is : {independent_check}")

        result1 = sum(avg_20) / len(avg_20)
        print(f"The average starting stock when the reorder point is 20 is: {result1}")
        result2 = sum(avg_30) / len(avg_30)
        print(f"The average starting stock when the reorder point is 30 is: {result2}")
        result3 = sum(avg_40) / len(avg_40)
        print(f"The average starting stock when the reorder point is 40 is: {result3}")
        result4 = sum(avg_50) / len(avg_50)
        print(f"The average starting stock when the reorder point is 50 is: {result4}")
        result5 = sum(avg_25) / len(avg_25)
        print(f"The average starting stock when the reorder point is 25 is: {result5}")
        result6 = sum(avg_35) / len(avg_35)
        print(f"The average starting stock when the reorder point is 35 is: {result6}")

        lost_result1 = sum(lost_20)
        print(f"The total lost units per day when the reorder point is 20 is: {lost_result1}")
        lost_result5 = sum(lost_25)
        print(f"The total lost units per day when the reorder point is 25 is: {lost_result5}")
        lost_result6 = sum(lost_35)
        print(f"The total lost units per day when the reorder point is 35 is: {lost_result6}")
        lost_result2 = sum(lost_30)
        print(f"The total lost units per day when the reorder point is 30 is: {lost_result2}")
        lost_result3 = sum(lost_40)
        print(f"The total lost units per day when the reorder point is 40 is: {lost_result3}")
        lost_result4 = sum(lost_50)
        return print(f"The total lost units per day when the reorder point is 50 is: {lost_result4}")


    _()




    # This version of the code includes an independent check at the end of every loop that checks the ending amount vs the initial starting stock of 60 + the sum of all deliveries - the total amount sold so that instead of a simulation that might get messy or mess up there is an independent list that checks the totals for each reorder point
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 7. Working With the Agent

    *Pick one piece of AI output you did not accept as-is. What did it give you, what did you change, and how did you know? Point to the commit or the cell.*

    *If the agent got it right the first time: what did you do to verify that?*
    """)
    return


@app.cell
def _():
    # I think the agent got most everyhting right when iasked it to adapt my code it used the code i had and just enhanced it. It added dumy variables like i did and kept the variable names and placements and definitions and loops i made everything i wrote the agent fixed or enhanced without removing or changing the core logic I had already implemented.

    #One aspect the agent did not do correctly is that after I made a rough draft and had initial code that included 60 for day 1 when i asked the agent to adapt and fix one problem, it created a new problem by replacing 60 with the calculated amount of 48 so I had to go back and replace values and try to reoder the print section and include the starting stock amount within the loop but then i encountered errors because there were other variables that were now out of order so it took some reordering with calling variables to that 60 appears for day 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 8. Going Further

    *Take at least one step past the main task, in any direction, and use your agent as much as you like. It does not have to work. State what you tried, what you found, and where it is in this notebook.*
    """)
    return


@app.cell
def _():
    def _():
        starting_stock = 60
        order_quantity = 100
        lead_time_days = 3
        reorder_points = range(10, 90, 10)  # 10, 20, 30, ..., 80
        daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,
                        9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]

        results = []  # this will become our list of records, our table

        for reorder_point in reorder_points:
            stock_list = []
            lost_list = []
            total_cost = 0

            starting_stock = 60
            order_pending = False
            days_since_order = 0

            for i in range(len(daily_demand)):
                if order_pending:
                    days_since_order += 1
                    if days_since_order == lead_time_days:
                        starting_stock += order_quantity
                        order_pending = False
                        days_since_order = 0

                sold_today = daily_demand[i]
                lost_today = 0
                if sold_today > starting_stock:
                    lost_today = sold_today - starting_stock
                    sold_today = starting_stock
                starting_stock -= sold_today

                if starting_stock <= reorder_point and not order_pending:
                    order_pending = True
                    days_since_order = 0
                    total_cost += 40  # cost of placing a reorder

                total_cost += starting_stock * 0.5  # cost of holding stock overnight
                total_cost += lost_today * 8        # cost of each lost unit

                stock_list.append(starting_stock)
                lost_list.append(lost_today)

            record = {
                "reorder_point": reorder_point,
                "avg_stock": sum(stock_list) / len(stock_list),
                "total_lost": sum(lost_list),
                "total_cost": total_cost,
            }
            results.append(record)

        print("Reorder Point", " "*5, "Avg Starting Stock", " "*5,
              "Total Lost Units", " "*5, "Total Cost")
        for record in results:
            print(record["reorder_point"], " "*15,
                  round(record["avg_stock"], 1), " "*15,
                  record["total_lost"], " "*15,
                  round(record["total_cost"], 2))


    _()
    return


if __name__ == "__main__":
    app.run()
