# 너무 더럽게 풀었다 ㅎ ㅎ , , 나중에 다시 정리할 것!
import sys

r,c,n = map(int,sys.stdin.readline().split())

graph = []
for _ in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))

if n%2 == 0:
    for _ in range(r):
        print('O'*c)

elif n == 1:
    for i in graph:
        print(''.join(i))

else:
    graph_all = []
    for _ in range(r):
        graph_all.append(['O']*c)

    for y in range(r):
        for x in range(c):
            if graph[y][x] == 'O':
                graph_all[y][x] = '.'

                if y-1 != -1:
                    graph_all[y-1][x] = '.'

                if x-1 != -1:
                    graph_all[y][x-1] = '.'

                if y+1 != r:
                    graph_all[y+1][x] = '.'

                if x+1 != c:
                    graph_all[y][x+1] = '.'
    if n%4 == 3:
        for i in graph_all:
            print(''.join(i))

    elif n%4 == 1:
        graph_all_new = []
        for _ in range(r):
            graph_all_new.append(['O']*c)

        for y in range(r):
            for x in range(c):
                if graph_all[y][x] == 'O':
                    graph_all_new[y][x] = '.'

                    if y - 1 != -1:
                        graph_all_new[y - 1][x] = '.'

                    if x - 1 != -1:
                        graph_all_new[y][x - 1] = '.'

                    if y + 1 != r:
                        graph_all_new[y + 1][x] = '.'

                    if x + 1 != c:
                        graph_all_new[y][x + 1] = '.'
        for i in graph_all_new:
            print(''.join(i))