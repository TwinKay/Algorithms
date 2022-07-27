import sys
total = sys.stdin.readlines()
for i in total:
    a, b = map(int, i.split())
    print(a+b)