h, l, a, b = map(int, input().split())
cond1 = h >= a / 2 and l >= b
cond2 = h >= b / 2 and l >= a

if cond1 or cond2:
    print("YES")
else:
    print("NO")