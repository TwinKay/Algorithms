import sys

N = int(sys.stdin.readline())
status = []
for _ in range(N):
    status.append(list(map(int,sys.stdin.readline().split())))

max_res = -1
for floor_num in range(1,7):
    down_side_val = floor_num
    sm = 0
    for i in range(N):
        down_side_idx = status[i].index(down_side_val)
        up_side_idx = 7 # dummy
        if down_side_idx == 0:
            up_side_idx = 5
        elif down_side_idx == 5:
            up_side_idx = 0
        elif down_side_idx == 1:
            up_side_idx = 3
        elif down_side_idx == 3:
            up_side_idx = 1
        elif down_side_idx == 2:
            up_side_idx = 4
        elif down_side_idx == 4:
            up_side_idx = 2

        up_side_val = status[i][up_side_idx]

        for cand in range(6,0,-1):
            if cand not in [down_side_val,up_side_val]:
                sm += cand
                break

        down_side_val = up_side_val

    max_res = max(max_res,sm)
print(max_res)


