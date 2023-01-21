def solution(k, score):
    import heapq as hq
    
    ans = []
    heap = []
    for i in score:
        if len(heap) >= k:
            if i >= heap[0]:
                hq.heappop(heap)
                hq.heappush(heap,i)
                ans.append(heap[0])
            else:
                ans.append(heap[0])
        else:
            hq.heappush(heap,i)
            ans.append(heap[0])

    return ans