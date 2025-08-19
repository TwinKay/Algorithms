import sys

delta_x = [0,1,0,-1]
delta_y = [-1,0,1,0]

T = int(sys.stdin.readline())
for _ in range(T):
    queries = list(sys.stdin.readline().rstrip())
    x,y = 0,0
    direct = 0
    min_x,min_y,max_x,max_y = 0,0,0,0
    for query in queries:
        if query == 'L':
            direct += 3
        elif query == 'R':
            direct += 1
        elif query == 'F':
            dx = x + delta_x[direct%4]
            dy = y + delta_y[direct%4]
            min_x = min(min_x,dx)
            max_x = max(max_x,dx)
            min_y = min(min_y,dy)
            max_y = max(max_y,dy)
            x,y = dx,dy
        else:
            dx = x - delta_x[direct%4]
            dy = y - delta_y[direct%4]
            min_x = min(min_x,dx)
            max_x = max(max_x,dx)
            min_y = min(min_y,dy)
            max_y = max(max_y,dy)
            x,y = dx,dy

    print((max_x-min_x)*(max_y-min_y))