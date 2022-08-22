import sys

total = [0,1]
for i in range(39):
    total.append(total[i]+total[i+1])

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:
        print('1 0')


    else:
        print(total[n-1],total[n])