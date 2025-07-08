import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = [-1]+arr

M = int(sys.stdin.readline())
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    if a==1:
        for i in range(1,N+1):
            if i%b==0:
                if arr[i]==0:
                    arr[i]=1
                else:
                    arr[i]=0
    else:
        if arr[b]==1:
            arr[b]=0
        else:
            arr[b]=1
        left = b-1
        right = b+1
        while left>0 and right<N+1:
            if arr[left]==arr[right]:
                if arr[left]==0:
                    arr[left]=1; arr[right]=1
                else:
                    arr[left]=0; arr[right]=0
            else:
                break
            left -= 1; right += 1
            

res = []
for a in arr[1:]:
    res.append(a)
    if len(res)==20:
        print(" ".join(map(str, res)))
        res.clear()
if res:
    print(" ".join(map(str, res)))