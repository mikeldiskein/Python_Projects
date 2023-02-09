n, m = [int(i) for i in input().split()]
matrix_1 = [[int(j) for j in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrix_2 = [[int(j) for j in input().split()] for _ in range(m)]
matrix_0 = []
for q in range(k):
    L = []
    for i in range(n):
        total = 0
        for j in range(m):
            total += matrix_1[i][j] * matrix_2[j][q]
        L.append(total)
    matrix_0.append(L)

for q in range(k):
    for i in range(n):
        print(matrix_0[i][q], end=' ')
    print()