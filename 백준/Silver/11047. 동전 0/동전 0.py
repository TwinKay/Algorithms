import sys

n, k = map(int, sys.stdin.readline().split())
total = []
for _ in range(n):
    total.append(int(sys.stdin.readline()))

t = 0
while True:
    if k == 0:
        break
    elif k >= total[n-1]:
        t += k // total[n-1]
        k = k % total[n-1]

    else:
        n -= 1

print(t)