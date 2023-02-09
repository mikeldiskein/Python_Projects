import time


# s = input().split()
# n, m = int(s[0]), int(s[1])
# matrix = []
# for i in range(n):
#     L = []
#     for j in range(m):
#         L.append((i+j) % m +1)
#     matrix.append(L)
# for i in range(n):
#     for j in range(m):
#         print(int(matrix[i][j]), end=' ')
#     print()


s = input().split()
begin = time.time()
n, m = int(s[0]), int(s[1])
matrix = [[' ' for _ in range(m)] for _ in range(n)]
MS = 0
for x in range(n+m):
    for i in range(n):
        for j in range(m):
            if i + j == x:
                MS += 1
                matrix[i][j] = MS
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()
end = time.time()
print(f'The program has run for {end-begin} seconds')