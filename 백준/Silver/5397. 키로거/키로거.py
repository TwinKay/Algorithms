# 출력을 더 예쁘게 할 수 있을 것 같은데..

import sys
from collections import deque

for i in range(int(sys.stdin.readline())):
    deq_left = deque()
    deq_right = deque()

    s = sys.stdin.readline().rstrip()

    for i in s:
        if i == '<':
            if deq_left:
                deq_right.appendleft(deq_left.pop())

        elif i == '>':
            if deq_right:
                deq_left.append(deq_right.popleft())

        elif i == '-':
            if deq_left:   # 문제에 해당 조건은 없으나..!
                deq_left.pop()

        else:
            deq_left.append(i)

    for i in deq_left:
        print(i, end='')

    if deq_right == deque([]):
        print('')
    else:
        for i in deq_right:
            print(i, end='')
        print('')