import sys

input = sys.stdin.readline
n = int(input().strip())
for _ in range(n):
    line = input().rstrip()
    stats = list(map(int, line.split()))
    count = sum(1 for x in stats if x >= 10)
    if count == 0:
        result = "zilch"
    elif count == 1:
        result = "double"
    elif count == 2:
        result = "double-double"
    else:
        result = "triple-double"
    print(line)
    print(result)
    print()