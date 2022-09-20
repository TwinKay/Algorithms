import sys

n = int(sys.stdin.readline())
exten = dict()

for i in range(n):
    a,b = sys.stdin.readline().rstrip().split('.')

    if b in exten.keys():
        exten[b] += 1
    else:
        exten[b] = 1

sort_exten = sorted(exten.items())

for x,y in sort_exten:
    print(x,y)