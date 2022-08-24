import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    total = [1,2,4]
    for i in range(n-3):
        total.append(total[i]+total[i+1]+total[i+2])

    print(total[n-1])