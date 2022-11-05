import sys

n = int(sys.stdin.readline())
energy = list(map(int, sys.stdin.readline().split()))

energy.sort()

res = energy.pop()
for i in range(n-1):
    b = energy[i]
    if res > b:
        res = b*(0.5) + res
    else:
        res = res*(0.5) + b

print(res)