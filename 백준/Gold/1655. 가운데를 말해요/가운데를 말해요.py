import sys
import heapq

small = []
big = []

for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())

    if len(small) == len(big):
        if len(small) == 0:
            heapq.heappush(small, (-a, a))
            print(a)

        elif small[0][1] <= a <= big[0][0]:
            heapq.heappush(small, (-a, a))
            print(a)

        elif a < small[0][1]:
            heapq.heappush(small, (-a, a))
            print(small[0][1])

        else:
            heapq.heappush(big, (a, a))

            c = heapq.heappop(big)
            heapq.heappush(small, (-c[0],c[1]))
            print(small[0][1])

    else:
        if len(big) == 0:
            if a >= small[0][1]:
                heapq.heappush(big, (a, a))
                print(small[0][1])
            else:
                c = heapq.heappop(small)
                
                heapq.heappush(big, (-c[0],c[1]))
                heapq.heappush(small, (-a, a))
                print(small[0][1])

        elif small[0][1] <= a <= big[0][0]:
            heapq.heappush(big, (a, a))
            print(small[0][1])

        elif a < small[0][1]:
            heapq.heappush(small, (-a, a))

            c = heapq.heappop(small)
            heapq.heappush(big, (-c[0], c[1]))
            print(small[0][1])

        else:
            heapq.heappush(big, (a, a))
            print(small[0][1])