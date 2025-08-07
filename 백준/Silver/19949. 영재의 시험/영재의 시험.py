import sys

def back_tracking(n,cnt,res):
    global total_cnt
    if n==10:
        if cnt >=5:
            total_cnt += 1
        return
    # if cnt >= 5: # 5점 이상
    #     total_cnt += 1
    #     return
    if cnt + (10-n) < 5: # 남은 문제를 다 맞춰도 5개 미만
        return
    if n<=1: # 초반 2개는 모든 경우
        for i in range(1,6):
            if arr[n] == i:
                back_tracking(n+1,cnt+1,res+[i])
            else:
                back_tracking(n+1,cnt,res+[i])
    else:
        for i in range(1,6):
            if res[-2] == res[-1] and res[-1] == i:
                continue
            if arr[n] == i:
                back_tracking(n+1,cnt+1,res+[i])
            else:
                back_tracking(n+1,cnt,res+[i])


arr = list(map(int, sys.stdin.readline().split()))
total_cnt = 0
back_tracking(0,0,[])
print(total_cnt)