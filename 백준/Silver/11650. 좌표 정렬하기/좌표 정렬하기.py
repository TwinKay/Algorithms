import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst = sorted(lst, key=lambda x: (x[0],x[1]))
for idx in lst:
    print(f'{idx[0]} {idx[1]}')