def solution(lottos, win_nums):
    
    cnt = 0
    cnt_zero = 0
    for i in lottos:
        if i == 0:
            cnt_zero += 1
        else:
            if i in win_nums:
                cnt += 1
    a,b = cnt+cnt_zero, cnt
    res = []
    if a == 6:
        res.append(1)
    elif a == 5:
        res.append(2)
    elif a == 4:
        res.append(3)
    elif a == 3:
        res.append(4)
    elif a == 2:
        res.append(5)
    else:
        res.append(6)
    if b == 6:
        res.append(1)
    elif b == 5:
        res.append(2)
    elif b == 4:
        res.append(3)
    elif b == 3:
        res.append(4)
    elif b == 2:
        res.append(5)
    else:
        res.append(6)

    return res