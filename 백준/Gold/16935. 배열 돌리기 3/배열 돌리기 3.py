'''
아이디어:
슬라이싱으로 풀기..! 슬라이싱 어렵다...............
'''
import sys

def flip_vert():
    global graph
    graph = graph[::-1]

def flip_hori():
    global graph
    graph = [graph[i][::-1] for i in range(N)]

def rotate_right():
    global graph,N,M
    graph = [list(e) for e in zip(*graph[::-1])]
    N,M = M,N

def rotate_left():
    global graph,N,M
    graph = [list(e) for e in zip(*graph)][::-1]
    N,M = M,N

def div_right():
    global graph
    half_N, half_M = N//2, M//2
    temp = [row[:half_M] for row in graph[:half_N]]

    for i in range(half_N):
        graph[i][:half_M] = graph[i + half_N][:half_M]

    for i in range(half_N):
        graph[i + half_N][:half_M] = graph[i + half_N][half_M:]

    for i in range(half_N):
        graph[i + half_N][half_M:] = graph[i][half_M:]

    for i in range(half_N):
        graph[i][half_M:] = temp[i]


def div_left():
    global graph
    half_N, half_M = N//2, M//2
    temp = [row[:half_M] for row in graph[:half_N]]

    for i in range(half_N):
        graph[i][:half_M] = graph[i][half_M:]

    for i in range(half_N):
        graph[i][half_M:] = graph[i + half_N][half_M:]

    for i in range(half_N):
        graph[i + half_N][half_M:] = graph[i + half_N][:half_M]

    for i in range(half_N):
        graph[i + half_N][:half_M] = temp[i]


N,M,R = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

queries = list(map(int, sys.stdin.readline().split()))
for query in queries:
    if query == 1: flip_vert()
    elif query == 2: flip_hori()
    elif query == 3: rotate_right()
    elif query == 4: rotate_left()
    elif query == 5: div_right()
    else: div_left()

for g in graph:
    print(*g)
