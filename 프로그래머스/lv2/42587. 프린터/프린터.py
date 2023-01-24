def solution(priorities, location):
    from collections import deque
    
    line = deque(list(range(len(priorities))))
    deq = deque(priorities)
    
    cnt = 0
    while deq:
        if deq[0] == max(deq):
            if line[0] == location:
                return cnt+1
            else:
                deq.popleft()
                line.popleft()
                cnt += 1
        else:
            deq.rotate(-1)
            line.rotate(-1)
