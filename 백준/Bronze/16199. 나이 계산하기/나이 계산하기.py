import sys

by, bm, bd, ty, tm, td = map(int, sys.stdin.read().split())

age_man = ty - by
if (tm, td) < (bm, bd):
    age_man -= 1

age_se = ty - by + 1
age_year = ty - by

print(age_man)
print(age_se)
print(age_year)