'''
아이디어:
분할정복 (1차 시간초과 -> 포함되는 범위로만 분할정복 및 남은 면 더해주기
'''
import sys

def div(x1,x2,y1,y2,each_siz):
    global cnt,is_find

    if is_find: # 찾으면 그만
        return

    if x2-x1 > 0: # 더 나눌수 있음
        mid_x = (x1+x2)//2
        mid_y = (y1+y2)//2

        if x1<=C<=mid_x and y1<=R<=mid_y:
            div(x1,mid_x,y1,mid_y,each_siz//4)
        elif mid_x+1<=C<=x2 and y1<=R<=mid_y:
            cnt += each_siz
            div(mid_x+1, x2, y1, mid_y,each_siz//4)
        elif x1<=C<=mid_x and mid_y+1<=R<=y2:
            cnt += each_siz*2
            div(x1,mid_x,mid_y+1,y2,each_siz//4)
        else:
            cnt += each_siz*3
            div(mid_x+1, x2, mid_y+1,y2,each_siz//4)
        return

    cnt += 1
    if x1==C and y1==R: # 찾음
        print(cnt-1)
        is_find = True


N,R,C = map(int, sys.stdin.readline().split())
cnt = 0
is_find = False
div(0,2**N-1,0,2**N-1,2**N*2**N//4)