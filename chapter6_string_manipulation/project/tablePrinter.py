tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


# Assume that all the inner lists will contain the same number of strings
def printTable(table):
    # check dimension
    WIDTH = len(table)
    HEIGHT = len(table[0])
    colRepWord = ""  # collumn representing word

    # create a grid to store column length value
    colWidth = [0] * len(table)
    for x in range(WIDTH):
        colRepWord = ""
        for y in range(HEIGHT):
            if len(table[x][y]) > len(colRepWord):
                colRepWord = table[x][y]

        # assign max colWidth for each col
        colWidth[x] = len(colRepWord)

    # away to print rows before columns
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # append with rjust()
            print(table[x][y].rjust(colWidth[x], " "), end=" ")
        print()


printTable(tableData)
