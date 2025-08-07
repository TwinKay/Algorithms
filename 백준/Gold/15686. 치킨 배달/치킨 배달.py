'''
아이디어:
최대 M개지만 M개로 고정하고 해도 된다. -> 치킨집이 더 적어서 최솟값이 갱신된는 경우 X
itertools 사용 -> 대신 index 자체로 넘기지 않고 index arr에 대한 index로 넘겨 시간 아끼기
'''
import sys
from itertools import combinations

def get_dist(x1,y1,x2,y2):
    '''
    맨해튼 거리를 반환하는 함수
    :param x1: 1지점의 x값
    :param y1: 1지점의 y값
    :param x2: 2지점의 x값
    :param y2: 2지점의 y값
    :return: (int) 두 지점의 맨해튼 거리
    '''
    return abs(x1-x2)+abs(y1-y2)

def get_idxs():
    '''
    집과 치킨집의 index들을 반환하는 함수
    :return: (list(list)) 집 indexs, 치킨집 indexs
    '''
    house_idxs = []
    chicken_idxs = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                house_idxs.append([j, i])
            elif graph[i][j] == 2:
                chicken_idxs.append([j, i])
    return [house_idxs,chicken_idxs]

def get_chicken_dist(chicken_sub_idxs):
    '''
    각 치킨집 idx 조합에 대한 도시의 치킨 거리(합)를 반환하는 코드
    :param chicken_sub_idxs: (tuple(int)) 치킨집 idx 조합 -> chicken_idxs의 idx로 입력
    :return: (int) 도시의 치킨 거리
    '''
    city_chicken_dist = 0
    for h_idx in house_idxs:
        min_dist = float('inf')
        for c_idx in chicken_sub_idxs:
            dist = get_dist(chicken_idxs[c_idx][0],chicken_idxs[c_idx][1],h_idx[0],h_idx[1])
            min_dist = min(min_dist,dist)
        city_chicken_dist += min_dist

    return city_chicken_dist

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

house_idxs, chicken_idxs = get_idxs()

min_chicken_dist = float('inf')
for comb in combinations(range(len(chicken_idxs)), M):
    chicken_dist = get_chicken_dist(comb)
    min_chicken_dist = min(min_chicken_dist,chicken_dist)

print(min_chicken_dist)
