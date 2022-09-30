import sys

s = sys.stdin.readline().rstrip()
minus = s.split('-')

for i,j in enumerate(minus):
    plus = j.split('+')

    cnt_plus = 0
    for k in plus:
        k = int(k)
        cnt_plus += k

    if i == 0:
        total_cnt = int(cnt_plus)
    else:
        total_cnt -= int(cnt_plus)

print(total_cnt)