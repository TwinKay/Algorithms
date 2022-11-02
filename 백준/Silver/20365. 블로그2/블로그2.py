import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
work = list(s)
work_b = s.split('R')
work_r = s.split('B')

cnt = 0
if work[0] == 'B':
    for i in work_r:
        if i != '':
            cnt += 1

else:
    for i in work_b:
        if i != '':
            cnt += 1

print(cnt+1)