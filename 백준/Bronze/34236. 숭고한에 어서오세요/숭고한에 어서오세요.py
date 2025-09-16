import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
diff = lst[1]-lst[0]
print(lst[-1]+diff)