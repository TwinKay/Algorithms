def is_red_line(x,y):
    if x==0 or x==N-1 or y==0 or y==N-1:
        return True
    return False

def init_direction(direct):
    arr = [None,0,2,1,3]
    return arr[direct]

def move(cell_dic):
    new_cell_dic = {}
    for key in cell_dic.keys():
        x,y = key
        val = cell_dic[key]
        for i in range(len(val)):
            cnt,direct = val[i]
            dx = x + delta_x[direct]
            dy = y + delta_y[direct]
            if is_red_line(dx,dy):
                if (dx,dy) in new_cell_dic.keys():
                    new_cell_dic[(dx,dy)].append([cnt//2,(direct+2)%4])
                else:
                    new_cell_dic[(dx,dy)] = [[cnt//2,(direct+2)%4]]
            else:
                if (dx,dy) in new_cell_dic.keys():
                    new_cell_dic[(dx,dy)].append([cnt,direct])
                else:
                    new_cell_dic[(dx,dy)] = [[cnt,direct]]
    return new_cell_dic

def merge(cell_dic):
    for key in cell_dic.keys():
        if len(cell_dic[key]) >= 2:
            cell_dic[key].sort(reverse=True)
            total_direct = cell_dic[key][0][1]
            total_cnt = 0
            for cnt,direct in cell_dic[key]:
                total_cnt += cnt
            cell_dic[key] = [[total_cnt,total_direct]]
    return cell_dic

def get_total_cnt(cell_dic):
    cnt = 0
    for key in cell_dic.keys():
        cnt += cell_dic[key][0][0]
    return cnt

delta_x = [0,-1,0,1]
delta_y = [-1,0,1,0]

TC = int(input())
for tc in range(1,TC+1):
    N,M,K = map(int, input().split())
    cell_dic = {}
    for _ in range(K):
        y,x,cnt,direct = map(int, input().split())
        if (x,y) in cell_dic.keys():
            cell_dic[(x,y)].append([cnt,init_direction(direct)])
        else:
            cell_dic[(x,y)] = [[cnt,init_direction(direct)]]

    for _ in range(M):
        cell_dic = move(cell_dic)
        cell_dic = merge(cell_dic)

    res = get_total_cnt(cell_dic)
    print(f'#{tc} {res}')
