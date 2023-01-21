def solution(s):
    cnt = 0
    cnt_t = 0
    cnt_f = 0
    for i in s:
        if cnt_t == 0:
            temp = i
        
        if i == temp:
            cnt_t += 1
        else:
            cnt_f += 1
            
        if cnt_t == cnt_f:
            cnt += 1
            cnt_t = 0
            cnt_f = 0
    if cnt_t == 0:
        return cnt
    else:
        return cnt+1