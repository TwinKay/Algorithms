import sys

def print_horses():
    for key in horses.keys():
        if horses[key]:
            print(f'{key}: {horses[key]}')

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def init_direction(direct):
    arr = [None,3,1,0,2]
    return arr[direct]

delta_x = [0,-1,0,1]
delta_y = [-1,0,1,0]

N,K = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

horses = {} # x,y -> [말 번호...]
for i in range(N):
    for j in range(N):
        horses[(j,i)] = []

horse_infos = [] # index가 말 번호 -> 항상 같이 업데이트
for k in range(K):
    y,x,direct = map(int, sys.stdin.readline().split())
    horses[(x-1,y-1)] = [k] # 말 번호(0부터)
    horse_infos.append([x-1,y-1,init_direction(direct)])

is_end = False
turn_cnt = 0
while True:
    if is_end: break
    turn_cnt += 1
    if turn_cnt == 1001:
        break

    # 여기에 반복문 넣어
    for horse_id in range(K):
        horse_x,horse_y,horse_direct = horse_infos[horse_id]
        horse_dx = horse_x + delta_x[horse_direct%4] # 한곳으로 바꾸자
        horse_dy = horse_y + delta_y[horse_direct%4]
        if not is_valid(horse_dx,horse_dy) or graph[horse_dy][horse_dx] == 2: # 범위 밖, 파랑
            horse_direct = (horse_direct+2)%4
            horse_infos[horse_id][2] = horse_direct
            horse_dx = horse_x + delta_x[horse_direct % 4]  # 한곳으로 바꾸자
            horse_dy = horse_y + delta_y[horse_direct % 4]
            if not is_valid(horse_dx,horse_dy) or graph[horse_dy][horse_dx] == 2: # 여전히 이동 x
                continue
            elif graph[horse_dy][horse_dx] == 0: # 흰색
                same_group = horses[(horse_x, horse_y)]
                horse_idx_in_group = same_group.index(horse_id)
                move_ids, horses[(horse_x, horse_y)] = same_group[horse_idx_in_group:], same_group[:horse_idx_in_group]
                horses[(horse_dx, horse_dy)].extend(move_ids)

                for move_id in move_ids:
                    horse_infos[move_id] = [horse_dx, horse_dy, horse_infos[move_id][2]]

                if len(horses[(horse_dx, horse_dy)]) >= 4:
                    is_end = True
                    break
            else: # 빨강
                same_group = horses[(horse_x, horse_y)]
                horse_idx_in_group = same_group.index(horse_id)
                move_ids, horses[(horse_x, horse_y)] = same_group[horse_idx_in_group:], same_group[:horse_idx_in_group]
                horses[(horse_dx, horse_dy)].extend(move_ids[::-1])

                for move_id in move_ids:
                    horse_infos[move_id] = [horse_dx, horse_dy, horse_infos[move_id][2]]

                if len(horses[(horse_dx, horse_dy)]) >= 4:
                    is_end = True
                    break

        elif graph[horse_dy][horse_dx] == 0:
            same_group = horses[(horse_x,horse_y)]
            horse_idx_in_group = same_group.index(horse_id)
            move_ids, horses[(horse_x,horse_y)] = same_group[horse_idx_in_group:],same_group[:horse_idx_in_group]
            horses[(horse_dx,horse_dy)].extend(move_ids)

            for move_id in move_ids:
                horse_infos[move_id] = [horse_dx,horse_dy,horse_infos[move_id][2]]

            if len(horses[(horse_dx, horse_dy)]) >= 4:
                is_end = True
                break

        else: # 빨강
            same_group = horses[(horse_x,horse_y)]
            horse_idx_in_group = same_group.index(horse_id)
            move_ids, horses[(horse_x,horse_y)] = same_group[horse_idx_in_group:],same_group[:horse_idx_in_group]

            horses[(horse_dx,horse_dy)].extend(move_ids[::-1])
            for move_id in move_ids:
                horse_infos[move_id] = [horse_dx,horse_dy,horse_infos[move_id][2]]

            if len(horses[(horse_dx, horse_dy)]) >= 4:
                is_end = True
                break

if turn_cnt == 1001:
    print(-1)
else:
    print(turn_cnt)