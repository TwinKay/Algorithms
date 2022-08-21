import sys

n = int(sys.stdin.readline())
t = 1
total = [1,1,1]


for i in range(97):
    total.append(total[i]+total[i+1])

for _ in range(n):
    print(total[int(sys.stdin.readline())-1])