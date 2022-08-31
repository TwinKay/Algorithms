import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    total = list(map(int,sys.stdin.readline().split()))
    count = [0]*10

    deq = deque()

    for i,j in enumerate(total):
        deq.append((j,i))
        count[9-j] += 1

    result = []
    for i in range(9):
        c = 0
        while True:
            if c == count[i]:
                break
            else:
                if deq[0][0] != 9-i:
                    deq.rotate(-1)
                else:
                    result.append(deq.popleft())
                    c += 1

    for i,j in enumerate(result):
        if j[1] == m:
            print(i+1)