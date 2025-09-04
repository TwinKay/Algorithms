import sys
from itertools import combinations
from collections import deque

def is_connect(st):
    cand = [0]*N
    for s in st:
        cand[s] = 1
    visited = [0]*N

    deq = deque()
    deq.append(st[0])
    visited[st[0]] = 1
    while deq:
        x = deq.popleft()
        for dx in graph[x]:
            if visited[dx]:
                continue
            if not cand[dx]:
                continue
            deq.append(dx)
            visited[dx] = 1
    cnt_visited = 0
    for v in visited:
        if v:
            cnt_visited += 1
    if cnt_visited == len(st):
        return True
    return False


def get_people_count(st):
    cnt = 0
    for s in st:
        cnt += cnt_people[s]
    return cnt

N = int(sys.stdin.readline())
cnt_people = list(map(int, sys.stdin.readline().split()))

graph = []
for i in range(N):
    graph.append([])
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for tp in temp[1:]:
        graph[i].append(tp-1)
        # graph[tp-1].append(i)

res_min = 10000
total_set = set(range(N))
for k in range(1,len(total_set)):
    for comb1 in combinations(total_set,k):
        if not is_connect(comb1):
            continue
        comb2 = total_set.difference(comb1)
        if not is_connect(tuple(comb2)):
            continue
        res_min = min(res_min,abs(get_people_count(comb1) - get_people_count(comb2)))

if res_min == 10000:
    print(-1)
else:
    print(res_min)