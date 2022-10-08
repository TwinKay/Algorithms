import sys
n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

result = [0,0,0]

def paper_number(x,y,n):
    jud = False
    a = graph[y][x]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if a != graph[j][i]:
                jud = True
                break

    if jud == False:
        if a == -1:
            result[0] += 1
        elif a == 0:
            result[1] += 1
        else:
            result[2] += 1

    else:
        paper_number(x, y, n//3)
        paper_number(x, y+n//3, n//3)
        paper_number(x, y+2*n//3, n//3)
        paper_number(x+n//3, y, n//3)
        paper_number(x+n//3, y+n//3, n//3)
        paper_number(x+n//3, y+2*n//3, n//3)
        paper_number(x+2*n//3, y, n//3)
        paper_number(x+2*n//3, y+n//3, n//3)
        paper_number(x+2*n//3, y+2*n//3, n//3)

paper_number(0,0,n)

for i in result:
    print(i)