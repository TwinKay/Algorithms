'''
행렬 곱
'''
import sys

N,M = map(int, sys.stdin.readline().split())
matrix_1 = []
for _ in range(N):
    matrix_1.append(list(map(int, sys.stdin.readline().split())))
M,K = map(int, sys.stdin.readline().split())
matrix_2 = []
for _ in range(M):
    matrix_2.append(list(map(int, sys.stdin.readline().split())))

res_arr = []
for _ in range(N):
    res_arr.append([])

for n in range(N):
    for k in range(K): # 2에만 적용
        val = 0
        for m in range(M):
            val += matrix_1[n][m] * matrix_2[m][k]
        res_arr[n].append(val)

for r in res_arr:
    print(*r)