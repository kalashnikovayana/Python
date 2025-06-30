rmatrix = [
    [5, 7, 9],
    [1, 2, 3],
    [4, 6, 8]
]

# for row in range(len(rmatrix)):
#     for col in range(len(rmatrix[row])):
#         if rmatrix[row][col] % 2 != 0:
#             rmatrix[row][col] = 0

# for row in range(len(rmatrix)):
#     rmatrix[row][0] = 0

# for col in range(len(rmatrix[-1])):
#     rmatrix[-1][col] = 0

for row in range(len(rmatrix)):
    for col in range(len(rmatrix[row])):
        if row == col:
            rmatrix[row][col] = 0

print(rmatrix)

        