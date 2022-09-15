import sys
from collections import deque

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.reverse()
deq = deque([])

for i in range(n):
    if num_list[i] == 1:
        deq.appendleft(i+1)

    elif num_list[i] == 2:
        deq.rotate(-1)  # 두 번째에 추가하기 위함
        deq.appendleft(i+1)
        deq.rotate(1)   # 다시 돌려놓기

    else:
        deq.append(i+1)

print(' '.join(list(map(str, deq))))