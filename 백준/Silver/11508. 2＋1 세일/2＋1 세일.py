import sys

n = int(sys.stdin.readline())

total = []
for _ in range(n):
    total.append(int(sys.stdin.readline()))
total.sort()

if len(total)%3 == 0:
    all = True
else:
    all = False

ans = 0
for _ in range(len(total)//3):
    l = []
    l.append(total.pop())
    l.append(total.pop())
    l.append(total.pop())
    l.sort(reverse=True)
    l.pop()
    ans += sum(l)


if all == True:
    print(ans)
else:
    print(ans + sum(total))