import sys

N, K = map(int, sys.stdin.readline().split())
ranks = list(map(int, sys.stdin.readline().split()))

grades = []
for g in ranks:
    p = (g * 100) // N
    if p <= 4:
        grades.append(1)
    elif p <= 11:
        grades.append(2)
    elif p <= 23:
        grades.append(3)
    elif p <= 40:
        grades.append(4)
    elif p <= 60:
        grades.append(5)
    elif p <= 77:
        grades.append(6)
    elif p <= 89:
        grades.append(7)
    elif p <= 96:
        grades.append(8)
    else:
        grades.append(9)

print(*grades)