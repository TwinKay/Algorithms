# 시험기간

import sys

l = []
while True:
    a = float(sys.stdin.readline())
    if a == 999:
        break
    else:
        l.append(a)
for i in range(len(l)-1):
    print("%.2f"%round(l[i+1]-l[i], 2))