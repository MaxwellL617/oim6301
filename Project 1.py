import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    starting_stock_initial = 60
    order_quantity = 100
    lead_time_days = 3
    reorder_points = [20, 30, 40, 50]
    daily_demand = [12,15,9,14,18,11,10,16,13,17,8,12,20,14,11,9,15,13,16,12,10,14,19,11,13,15,9,12,17,14,]

    avg_20 = []
    avg_30 = []
    avg_40 = []
    avg_50 = []

    lists = [avg_20, avg_30, avg_40, avg_50]

    for z in range(len(reorder_points)):
        starting_stock = starting_stock_initial
        lead_a = 0
        lead_b = 0
        lead_c = 0
        total_cost = 0

        def lead_calc():
            global starting_stock
            global arri
            global total_cost
            starting_stock += 100
            arri = 100
        #if reorder_points[z] == 40:
        print(f"\n--- SIMULATION TABLE FOR REORDER POINT {reorder_points[z]} ---")
        print(f"{'Day':<5} {'Start Stock':<13} {'Arrived':<9} {'Demand':<8} {'Sold':<6} {'Lost':<6} {'Ending Stock':<13} {'Units Ordered':<13}")
        print("-" * 80)
        for i in range(len(daily_demand)):
            day = i + 1
            arri = 0
            ordered = 0
            lost_units = 0

            if lead_a > 0:
                lead_a += 1
                if lead_a == 3:
                    lead_calc()
                    lead_a = 0
            if lead_b > 0:
                lead_b += 1
                if lead_b == 3:
                    lead_calc()
                    lead_b = 0
            if lead_c > 0:
                lead_c += 1
                if lead_c == 3:
                    lead_calc()
                    lead_c = 0
            start_day_stock = starting_stock
            demand_today = daily_demand[i]
            sold = min(start_day_stock, demand_today)
            lost_units = demand_today - sold
            ending_stock = start_day_stock - sold
            starting_stock = ending_stock
            if starting_stock <= reorder_points[z]:
                if lead_a == 0:
                    lead_a = 1
                    ordered = 100
                elif lead_b == 0:
                    lead_b = 1
                    ordered = 100
                elif lead_c == 0:
                    lead_c = 1
                    ordered = 100
            total_cost += starting_stock * 0.5
            if reorder_points[z] == 40:
                print(f"{day:<5} {start_day_stock:<13} {arri:<9} {demand_today:<8} {sold:<6} {lost_units:<6} {ending_stock:<13} {ordered:<13}")
            lists[z].append(ending_stock)

    print("\n" + "=" * 50)
    print(f"The average ending stock when the reorder point is 20 is: {sum(avg_20)/len(avg_20):.2f}")
    print(f"The average ending stock when the reorder point is 30 is: {sum(avg_30)/len(avg_30):.2f}")
    print(f"The average ending stock when the reorder point is 40 is: {sum(avg_40)/len(avg_40):.2f}")
    print(f"The average ending stock when the reorder point is 50 is: {sum(avg_50)/len(avg_50):.2f}")
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
