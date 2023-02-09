n, m = (int(i) for i in input().split())

matrix = [[0] * m for _ in range(n)]
counter = 1
passed_columns, passed_rows = 0, 0
current_column, current_row = 0, 0


# i = n = rows, j = m = columns
for k in range(n * m):
    if counter > n * m:
        break
    direction = k % 4
    if direction == 0:
        for j in range(passed_columns, m - passed_columns):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
        passed_rows += 1
    elif direction == 1:
        for i in range(passed_rows, n - passed_rows + 1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i
        passed_columns += 1
    elif direction == 2:
        for j in range(current_column - 1, passed_columns - 2, - 1):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
    elif direction == 3:
        for i in range(current_row - 1, passed_rows - 1, - 1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i


for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()





