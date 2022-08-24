import sys

w,h,x,y,p = map(int, sys.stdin.readline().split())

t = 0
for _ in range(p):

    a,b = map(int, sys.stdin.readline().split())

    if ((a-x)**2 + (b-(y+h*0.5))**2)**0.5 <= h*0.5:  # 왼쪽 반원
        t += 1
    elif ((a-(x+w))**2 + (b-(y+h*0.5))**2)**0.5 <= h*0.5:  # 오른쪽 반원
        t += 1
    elif x <= a <= x+w and y <= b <= y+h:  # 직사각형
        t += 1

print(t)