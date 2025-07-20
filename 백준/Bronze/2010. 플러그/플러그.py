import sys

data = sys.stdin.read().split()
N = int(data[0])
plugs = map(int, data[1:])
print(sum(plugs) - (N - 1))