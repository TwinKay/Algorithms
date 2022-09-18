import sys

total = [0]*10
s = sys.stdin.readline().rstrip()

for i in s:
    total[int(i)] += 1

total[6] = (total[6]+total.pop())/2

if max(total)%1 != 0:    # 파이썬 round는 binary arithmetic 방식 사용
    print(int(max(total)+0.5))
else:
    print(int(max(total)))