# 조금 더 예쁘게 만들 수 있을 것 같은데..

import sys
import heapq

for _ in range(int(sys.stdin.readline())):

    n = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    visited = [False]*1000000

    for i in range(n):
        a,b = sys.stdin.readline().split()
        b = int(b)

        if a == 'I':
            heapq.heappush(min_heap, (b,i))
            heapq.heappush(max_heap, (-b,i))
            visited[i] = True

        else:
            if b == -1:
                while True:
                    if min_heap == []:
                        break
                    elif visited[min_heap[0][1]] == False:
                        heapq.heappop(min_heap)
                    else:
                        visited[min_heap[0][1]] = False
                        heapq.heappop(min_heap)
                        break

            else:
                while True:
                    if max_heap == []:
                        break
                    elif visited[max_heap[0][1]] == False:
                        heapq.heappop(max_heap)
                    else:
                        visited[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
                        break

    while True:
        if min_heap == []:
            break
        elif visited[min_heap[0][1]] == False:
            heapq.heappop(min_heap)
        else:
            break

    while True:
        if max_heap == []:
            break
        elif visited[max_heap[0][1]] == False:
            heapq.heappop(max_heap)
        else:
            break

    if visited == [False]*1000000:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])