import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
cnt_total = 0
min_time = 200000

visited = [False]*100001

# dir = 0 : -1 , dir = 1 : +1
deq = deque([[n,0,False,0]])
while deq:
    p, cnt, fix, dir = deq.popleft()

    visited[p] = True
    
    if min_time < cnt:
        break
    
    if p == k:
        cnt_total += 1
        min_time = cnt
    else:
        if fix:
            if dir == 0:
                if 0 <= p-1 <= 100000:
                    if not visited[p-1]:
                        deq.append([p-1,cnt+1,True,0])
            else:
                if 0 <= p+1 <= 100000:
                    if not visited[p+1]:
                        deq.append([p+1,cnt+1,True,1])
            if 0 <= p*2 <= 100000:
                if not visited[p*2]:
                    deq.append([p*2,cnt+1,False,0])
        else:
            if 0 <= p-1 <= 100000:
                if not visited[p-1]:
                    deq.append([p-1,cnt+1,True,0])
            if 0 <= p+1 <= 100000:
                if not visited[p+1]:
                    deq.append([p+1,cnt+1,True,1])
            if 0 <= p*2 <= 100000:
                if not visited[p*2]:
                    deq.append([p*2,cnt+1,False,0])
        
print(min_time)
print(cnt_total)