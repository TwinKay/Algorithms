import sys

s = sys.stdin.readline().rstrip()
res = 0
for c in s:
    asc = ord(c)-65
    if asc<=2:
        res += 3
    elif asc<=5:
        res += 4
    elif asc<=8:
        res += 5
    elif asc<=11:
        res += 6
    elif asc<=14:
        res += 7
    elif asc<=18:
        res += 8
    elif asc<=21:
        res += 9
    else:
        res += 10
print(res)