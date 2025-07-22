import sys

N = int(sys.stdin.readline())
dif = [int(sys.stdin.readline()) for _ in range(N)]

first = dif[0]
minimum = min(dif)
maximum = max(dif)

if first == minimum:
    print("ez")
elif first == maximum:
    print("hard")
else:
    print("?")
