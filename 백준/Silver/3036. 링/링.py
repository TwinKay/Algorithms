import sys

n = int(sys.stdin.readline())
total = list(map(int, sys.stdin.readline().split()))

for i in range(1,n):
    a = total[0] ; b = total[i]

    while b>0:
        a,b = b,a%b

    print(str(total[0]//a)+'/'+str(total[i]//a))