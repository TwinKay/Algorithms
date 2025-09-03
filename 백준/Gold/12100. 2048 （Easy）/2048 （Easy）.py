'''
한 방향 기준으로만 작성해서 rotate해서 사용! -> 편하게 짜고 실수 줄이기
=> 시간 충분하다! 뭐 불안하면 rotate만 한번에 돌려주던지.. -> 일단 한 방향으로 k번 돌리도록
'''
'''
한 방향 기준으로만 작성해서 rotate해서 사용! -> 편하게 짜고 실수 줄이기
=> 시간 충분하다! 뭐 불안하면 rotate만 한번에 돌려주던지.. -> 일단 한 방향으로 k번 돌리도록
'''
# 1차 코드
# import sys
#
# def rotate(graph): # 우측 90도
#     new_graph = []
#     for j in range(N):
#         new_graph.append([])
#         for i in range(N-1,-1,-1):
#             new_graph[j].append(graph[i][j])
#     return new_graph
#
# def move_each(lst):
#     temp = []
#     for l in lst:
#         if l:
#             temp.append(l)
#     new_line = []
#
#     is_find = False
#     for i in range(len(temp)):
#         if is_find:
#             is_find = False
#             continue
#
#         if i == len(temp)-1:
#             new_line.append(temp[i])
#         elif temp[i] == temp[i+1]:
#             new_line.append(temp[i]*2)
#             is_find = True
#         else:
#             new_line.append(temp[i])
#
#     for _ in range(N-len(new_line)):
#         new_line.append(0)
#
#     return new_line
#
# def move(graph,direct):
#     if direct != 0:
#         for _ in range(direct):
#             graph = rotate(graph)
#
#     for i in range(N):
#         graph[i] = move_each(graph[i])
#
#     if direct != 0:
#         for _ in range(4-direct):
#             graph = rotate(graph)
#
#     return graph
#
# N = int(sys.stdin.readline())
# origin_graph = []
# for _ in range(N):
#     origin_graph.append(list(map(int, sys.stdin.readline().split())))
#
# res_max = 0
# for a in range(4):
#     for b in range(4):
#         for c in range(4):
#             for d in range(4):
#                 for e in range(4):
#                     graph = [g for g in origin_graph[:]]
#                     graph = move(graph,a)
#                     graph = move(graph,b)
#                     graph = move(graph,c)
#                     graph = move(graph,d)
#                     graph = move(graph,e)
#
#                     val_max = 0
#                     for i in range(N):
#                         for j in range(N):
#                             val_max = max(val_max,graph[i][j])
#                     res_max = max(res_max,val_max)
#
# print(res_max)


# 2차 코드: 1차 코드보다 실행 시간은 더 빠르겠지만 1차 코드가 더 작성 시간이 빠르고 실수를 줄이는 방법이라 생각
import sys

def rotate90(graph): # 우측 90도
    new_graph = []
    for j in range(N):
        new_graph.append([])
        for i in range(N-1,-1,-1):
            new_graph[j].append(graph[i][j])
    return new_graph

def rotate180(graph): # 우측 180도
    new_graph = []
    for _ in range(N):
        new_graph.append([])
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            new_graph[N-i-1].append(graph[i][j])
    return new_graph

def rotate270(graph): # 우측 270도
    new_graph = []
    for j in range(N):
        new_graph.append([])
        for i in range(N-1,-1,-1):
            new_graph[j].append(graph[N-i-1][j])
    return new_graph

def move_each(lst):
    temp = [] # 0은 빼고 임시 저장
    for l in lst:
        if l:
            temp.append(l)

    new_line = [] # 병합할 라인
    is_find = False # 병합되면 for문 idx 하나 건너뛰기 위함
    for i in range(len(temp)):
        if is_find: # 병합이면 하나 건너뛰기
            is_find = False
            continue

        if i == len(temp)-1: # 맨 마지막 혼자인 경우 index error 방지
            new_line.append(temp[i])
        elif temp[i] == temp[i+1]: # 같으면
            new_line.append(temp[i]*2)
            is_find = True
        else: # 병합x
            new_line.append(temp[i])

    for _ in range(N-len(new_line)): # 0 채우기
        new_line.append(0)

    return new_line

def move(graph,direct):
    if direct == 1:
        graph = rotate90(graph)
    elif direct == 2:
        graph = rotate180(graph)
    elif direct == 3:
        graph = rotate270(graph)
    # 0은 돌 필요 x


    for i in range(N):
        graph[i] = move_each(graph[i])

    # 여기는 원복이니깐 합이 360 이도록
    if direct == 1:
        graph = rotate270(graph)
    elif direct == 2:
        graph = rotate180(graph)
    elif direct == 3:
        graph = rotate90(graph)

    return graph

N = int(sys.stdin.readline())
origin_graph = []
for _ in range(N):
    origin_graph.append(list(map(int, sys.stdin.readline().split())))

res_max = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4): # 뭐 동적이지도 않으니깐 5중 for문..
                    graph = [g for g in origin_graph[:]]
                    graph = move(graph,a)
                    graph = move(graph,b)
                    graph = move(graph,c)
                    graph = move(graph,d)
                    graph = move(graph,e)

                    val_max = 0
                    for i in range(N):
                        for j in range(N):
                            val_max = max(val_max,graph[i][j])
                    res_max = max(res_max,val_max)

print(res_max)