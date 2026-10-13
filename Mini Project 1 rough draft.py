import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import random
    import matplotlib.pyplot as plt


    starting_stock = 60
    order_quantity = 100
    lead_time_days = 3
    reorder_points = [20, 30, 40, 50]
    demand = []
    costs = []

    added_stock = 0
    reorder_wait_a = 0
    reorder_wait_b = 0

    days = []
    held_stock = []

    total_cost = 0

    print("Kept Stock"," "*10, "Demand"," "*10, "Remaining Stock", " "*10, "Added Stock")


    for i in range(365):
        total_cost += starting_stock * .5
        daily_demand = random.randint(5,20)
        print(starting_stock," "*20 ,daily_demand, " "*20 ,starting_stock-daily_demand)
        starting_stock -= daily_demand
        if starting_stock <= 20 or starting_stock <= 30 or starting_stock <= 40 or starting_stock <= 50:
            reorder_wait_a += 1
            added_stock = 0
            if reorder_wait_a > 1:
                reorder_wait_b += 1
                if reorder_wait_b == 3:
                    starting_stock += 100
                    added_stock +=100
                    reorder_wait_b = 0
                    total_cost += 8
            if reorder_wait_a == 3:
                starting_stock += 100
                added_stock +=100
                reorder_wait_a = 0
                total_cost += 8
            print(" "*65, added_stock)
        days.append(i+1)
        held_stock.append(starting_stock)
        demand.append(daily_demand)
        costs.append(total_cost)



    def plot_stock_data(y_values, title="Data Over Time", y_label="Value"):
        plt.plot(days, y_values, color="blue", marker="o", linestyle="-")

        plt.title(title)
        plt.xlabel("Days")
        plt.ylabel(y_label)

        plt.show()


    plot_stock_data(held_stock, title="Stock Kept Over Time", y_label="Stock Held")

    plot_stock_data(costs, title="Cost Over Time", y_label="Total Cost")



    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
