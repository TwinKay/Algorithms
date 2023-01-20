def solution(numbers, target):
    from collections import deque

    n = len(numbers)
    res = 0

    deq = deque([])
    deq.append([numbers[0],0])
    deq.append([-numbers[0],0])
    while deq:
        x,cnt = deq.popleft()
        if cnt == n-1:
            if x == target:
                res += 1

        else:
            if x+sum(numbers[cnt+1:]) >= target:
                deq.append([x+numbers[cnt+1],cnt+1])
            if x-sum(numbers[cnt+1:]) <= target:
                deq.append([x-numbers[cnt+1], cnt+1])

    return res