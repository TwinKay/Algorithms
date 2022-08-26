# 진짜 큐(데크)로 구현하는 문제였다..

import sys
from collections import deque

total = deque([])

for _ in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().strip()
    if x[:2] == 'pu':
        a,b = x.split()
        total.append(int(b))

    else:
        if x == 'pop':
            if total != deque([]):
                print(total.popleft())
            else:
                print(-1)

        elif x == 'size':
            print(len(total))

        elif x == 'empty':
            if total == deque([]):
                print(1)
            else:
                print(0)

        elif x == 'front':
            if total != deque([]):
                print(total[0])
            else:
                print(-1)

        else:
            if total != deque([]):
                print(total[-1])
            else:
                print(-1)