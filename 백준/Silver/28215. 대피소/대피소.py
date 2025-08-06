import sys

def get_dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

N,K = map(int, sys.stdin.readline().split())
house_idxs = []
for _ in range(N):
    house_idxs.append(list(map(int, sys.stdin.readline().split())))

def back_tracking(n,start,res):
    global res_min
    if n==K:
        temp_max = -1
        for house_idx in house_idxs:
            temp_min = float('inf')
            for r in res:
                dist = get_dist(house_idx[0],house_idx[1],house_idxs[r][0],house_idxs[r][1])
                temp_min = min(temp_min,dist)
            temp_max = max(temp_max, temp_min)
        res_min = min(res_min,temp_max)
        return

    for i in range(start,N):
        res.append(i)
        back_tracking(n+1,i+1,res)
        res.pop()

res_min = float('inf')
back_tracking(0,0,[])
print(res_min)