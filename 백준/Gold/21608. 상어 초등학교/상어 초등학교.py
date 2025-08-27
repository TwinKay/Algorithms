import sys

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append([0]*N)

favorite_dic = {}
order_student = []

for _ in range(N*N):
    num, a,b,c,d = map(int, sys.stdin.readline().split())
    favorite_dic[num] = {a, b, c, d}
    order_student.append(num)

for student_id in order_student:

    max_favorite_cnt = -1
    max_blank_cnt = -1
    best_x,best_y = N,N
    for i in range(N): # 행 우선 -> 같을 떄 갱신 X
        for j in range(N):
            if graph[i][j] != 0: continue

            favorite_cnt = 0
            blank_cnt = 0
            favorite_set = favorite_dic[student_id]
            for k in range(4):
                dx = j + delta_x[k]
                dy = i + delta_y[k]
                if not is_valid(dx,dy):
                    continue

                if graph[dy][dx] == 0:
                    blank_cnt += 1
                elif graph[dy][dx] in favorite_set:
                    favorite_cnt += 1

            if favorite_cnt > max_favorite_cnt:
                max_favorite_cnt = favorite_cnt
                max_blank_cnt = blank_cnt
                best_x, best_y = j,i
            elif favorite_cnt == max_favorite_cnt:
                if max_blank_cnt < blank_cnt:
                    max_blank_cnt = blank_cnt
                    best_x, best_y = j, i

    graph[best_y][best_x] = student_id

res = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        favorite_set = favorite_dic[graph[i][j]]
        for k in range(4):
            dx = j + delta_x[k]
            dy = i + delta_y[k]
            if is_valid(dx,dy):
                if graph[dy][dx] in favorite_set:
                    cnt += 1

        if cnt == 1:
            res += 1
        elif cnt == 2:
            res += 10
        elif cnt == 3:
            res += 100
        elif cnt == 4:
            res += 1000

print(res)