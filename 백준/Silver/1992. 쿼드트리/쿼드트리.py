import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

def div(x,y,n):
    s = set()
    for i in graph[y:y+n]:
        for j in i[x:x+n]:
            s.add(j)

    if len(s) == 1:
        print(s.pop(), end='')
    else:
        print('(', end='')
        div(x, y, n//2)
        div(x+n//2, y, n//2)
        div(x, y+n//2, n//2)
        div(x+n//2, y+n//2, n//2)
        print(')', end='')

div(0,0,n)