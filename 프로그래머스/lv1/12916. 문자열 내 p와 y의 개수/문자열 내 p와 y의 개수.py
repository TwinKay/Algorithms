def solution(s):
    cnt_p = 0
    cnt_y = 0
    for i in s:
        if i == 'p' or i == 'P':
            cnt_p += 1
        elif i == 'y' or i == 'Y':
            cnt_y += 1
            
    if cnt_p == cnt_y:
        ans = True
    else:
        ans = False
    return ans