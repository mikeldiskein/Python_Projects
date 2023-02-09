from time import time
start = time()
side = 20
matrix = [[0 for _ in range(side + 1)] for _ in range(side + 1)]


def count_paths(matrix, row, col):
    if row == 0 or col == 0:
        return 1
    return count_paths(matrix, row - 1, col) + count_paths(matrix, row, col - 1)


print(count_paths(matrix=matrix, row=side, col=side))
end = time()
print(f'Time: {end - start}')


