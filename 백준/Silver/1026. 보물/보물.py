import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()

result = 0
for i in A:
    result += i * B.pop(B.index(max(B)))

print(result)