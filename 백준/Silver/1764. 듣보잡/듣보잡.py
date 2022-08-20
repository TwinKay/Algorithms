import sys

a, b = map(int, sys.stdin.readline().split())

a_set = set()
for i in range(a):
    a_set.add(sys.stdin.readline().strip())

b_set = set()
for i in range(b):
    b_set.add(sys.stdin.readline().strip())

result = list(a_set & b_set)
result.sort()

print(len(result))
for i in result:
    print(i)