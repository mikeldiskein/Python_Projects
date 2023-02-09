n = 1001
matrix = [[0 for _ in range(n)] for i in range(n)]


y, x = n // 2, n // 2
row, col = y, x
matrix[row][col] = 1

direction = 'right'
diff = 1
number = 2
for _ in range(n * n - 1):
    if direction == 'right':
        row, col = row, col + 1
        matrix[row][col] = number
        if abs(col - x) == diff or (abs(col - x) == diff and abs(row - y) == diff):
            direction = 'down'
            number += 1
        else:
            number += 1
    elif direction == 'down':
        row, col = row + 1, col
        matrix[row][col] = number
        if abs(col - x) == diff and abs(row - y) == diff:
            direction = 'left'
            number += 1
        else:
            number += 1
    elif direction == 'left':
        row, col = row, col - 1
        matrix[row][col] = number
        if abs(col - x) == diff and abs(row - y) == diff:
            direction = 'up'
            number += 1
        else:
            number += 1
    elif direction == 'up':
        row, col = row - 1, col
        matrix[row][col] = number
        if abs(col - x) == diff and abs(row - y) == diff:
            direction = 'right'
            number += 1
            diff += 1
        else:
            number += 1


for j in range(len(matrix)):
    print(matrix[j])

ans = 0
for i in range(len(matrix[row])):
    for j in range(len(matrix[col])):
        if i == j:
            ans += matrix[i][j]
        elif i + j == n - 1:
            ans += matrix[i][j]

print(ans)

