import sys

total = []
for _ in range(int(sys.stdin.readline())):

    a = int(sys.stdin.readline())
    if a != 0:
        total.append(a)
    else:
        total.pop()
print(sum(total))