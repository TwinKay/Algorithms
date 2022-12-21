import sys

total = []

n = int(sys.stdin.readline())
for _ in range(n):
    a,b,c = map(int, sys.stdin.readline().split())

    if a==b and b==c and a==c:
        total.append(10000+a*1000)
    elif a==b:
        total.append(1000+a*100)
    elif b==c:
        total.append(1000+b*100)
    elif a==c:
        total.append(1000+a*100)
    else:
        total.append(max(a,b,c)*100)
print(max(total))