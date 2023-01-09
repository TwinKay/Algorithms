import sys
s = sys.stdin.readline().rstrip()
res = []
for i in s:
    if i.isupper():
        res.append(i.lower())
    else:
        res.append(i.upper())
print(''.join(res))