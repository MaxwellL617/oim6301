import marimo

__generated_with = "0.24.2"
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
    return


if __name__ == "__main__":
    app.run()
