import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
max = -1
for i in range(N-3):
    for j in range(i+1,N-2):
        for k in range(j+1,N-1):
            group1 = 1; group2 = 1; group3 = 1; group4 = 1
            for a in range(i+1):
                group1 *= arr[a]
            for b in range(i+1,j+1):
                group2 *= arr[b]
            for c in range(j+1,k+1):
                group3 *= arr[c]
            for d in range(k+1,N):
                group4 *= arr[d]
            total = group1+group2+group3+group4
            if total>max:
                max = total
print(max)