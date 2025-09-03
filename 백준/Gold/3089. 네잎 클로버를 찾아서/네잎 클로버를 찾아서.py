import sys
from bisect import bisect_left

N,M = map(int, sys.stdin.readline().split())
x_dic = {}
y_dic = {}
for _ in range(N):
    x,y = map(int, sys.stdin.readline().split())
    if x in x_dic:
        x_dic[x].append(y)
    else:
        x_dic[x] = [y]
    if y in y_dic:
        y_dic[y].append(x)
    else:
        y_dic[y] = [x]

for key in x_dic:
    x_dic[key].sort()
for key in y_dic:
    y_dic[key].sort()

x,y = 0,0
queries = list(sys.stdin.readline().rstrip())
for query in queries:
    if query == 'R':
        idx = bisect_left(y_dic[y],x,0,len(y_dic[y])-1)
        x = y_dic[y][idx+1]
    elif query == 'L':
        idx = bisect_left(y_dic[y],x,0,len(y_dic[y])-1)
        x = y_dic[y][idx-1]
    elif query == 'U':
        idx = bisect_left(x_dic[x],y,0,len(x_dic[x])-1)
        y = x_dic[x][idx+1]
    elif query == 'D':
        idx = bisect_left(x_dic[x],y,0,len(x_dic[x])-1)
        y = x_dic[x][idx-1]
        
print(x,y)