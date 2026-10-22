import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    dict = {"Max":1, "Ben":2, "Dan":3}

    print(dict["Max"])
    return


app._unparsable_cell(
    r"""
    lists = [,2,3,4,5]
    """,
    name="_"
)


@app.cell
def _():
    names_dict = [
        {'name':'Max', 'age': 25}, {'name':'Ben', 'age': 30}, {'name':'Sam', 'age': 35}, {'name': 'Dan', 'age': 21}
    ]

    print(names_dict[1]['name'])
    index = -1
    your_name = input("Enter your name").capitalize()

    for row in names_dict:
        index +=1
        if names_dict[index]['name'] == 'Max':
            print(names_dict[index]['name'], names_dict[index]['age'])


    return


app._unparsable_cell(
    r"""
    for rows in 
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
