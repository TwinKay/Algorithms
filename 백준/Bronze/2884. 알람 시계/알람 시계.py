import sys

h,m = map(int, sys.stdin.readline().split())
total_m = h*60 + m
total_m -= 45
if total_m < 0:
    total_m += 24*60
res = ""
res += str(total_m // 60)
res += " "
res += str(total_m % 60)
print(res)