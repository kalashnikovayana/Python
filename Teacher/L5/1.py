rmatrix = [
    [5, 7, 9],
    [1, 2, 3],
    [4, 6, 8]
]

for row_index in range(len(rmatrix)):
    for col_index in range(len(rmatrix[row_index])):
        if row_index == len(rmatrix)-1-col_index: