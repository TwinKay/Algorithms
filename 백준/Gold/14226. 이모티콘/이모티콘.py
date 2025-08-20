import sys
from collections import deque

def is_valid(x):
    return 0<=x<len(visited)

S = int(sys.stdin.readline())

visited = [False]*(S*2+10) # 안전하게 10(-1 index로 클립보드 없는 경우도 사용)
visited = []
for i in range(S*2+10):
    visited.append([False]*(S*2+10))

deq = deque()
deq.append([1,-1,0])
visited[1][-1] = True
while deq:
    num,clip_val,time = deq.popleft()
    if num == S:
        print(time)
        break

    if not visited[num][num]:
        deq.append([num,num,time+1])
        visited[num][num] = True
    if clip_val != -1 and is_valid(num+clip_val) and not visited[num+clip_val][clip_val]: # 붙
        deq.append([num+clip_val,clip_val,time+1])
        visited[num+clip_val][clip_val] = True
    if is_valid(num-1) and not visited[num-1][clip_val]: # 하나 지우기
        deq.append([num-1,clip_val,time+1])
        visited[num-1][clip_val] = True