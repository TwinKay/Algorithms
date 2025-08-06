import sys

def get_dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

N,K = map(int, sys.stdin.readline().split())
house_idxs = []
for _ in range(N):
    house_idxs.append(list(map(int, sys.stdin.readline().split())))

def back_tracking(n,start,res):
    global min_val, real_res
    if n==K:
        d_idxs = []
        h_idxs = []
        for r in res:
            d_idxs.append(house_idxs[r])
        for house_idx in house_idxs:
            if house_idx not in d_idxs:
                h_idxs.append(house_idx)
        max_val = -1
        for h_idx in h_idxs:
            temp = float('inf')
            for d_idx in d_idxs:
                temp = min(temp,get_dist(d_idx[0],d_idx[1],h_idx[0],h_idx[1]))
            max_val = max(max_val,temp)

        real_res = min(real_res,max_val)


        return

    for i in range(start,N):
        back_tracking(n+1,i+1,res+[i])

visited = [False]*N
real_res = float('inf')
back_tracking(0,0,[])

print(real_res)