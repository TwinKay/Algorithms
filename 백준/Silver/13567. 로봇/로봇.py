'''
M+1 꼭 !!
'''
import sys

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

# 우 하 좌 상
delta_x = [1,0,-1,0]
delta_y = [0,1,0,-1]

N,Q = map(int, sys.stdin.readline().split())
N += 1
direct = 0
x,y = 0,N-1
is_posi = True
for _ in range(Q):
    query,num = sys.stdin.readline().split()
    num = int(num)

    if query =='MOVE':
        dx = x + delta_x[direct%4]*num
        dy = y + delta_y[direct%4]*num
        if is_valid(dx,dy):
            x,y = dx,dy
        else:
            is_posi = False
            break

    else:
        if num == 0:
            direct += 3
        else:
            direct += 1

if is_posi:
    print(x,N-1-y)
else:
    print(-1)