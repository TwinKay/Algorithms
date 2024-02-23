def solution(answers):
    stu_1 = [1,2,3,4,5]
    stu_2 = [2,1,2,3,2,4,2,5]
    stu_3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt_1 = 0 ; cnt_2 = 0 ; cnt_3 = 0
    
    for i in range(len(answers)):
        if answers[i] == stu_1[(i%5)]:
            cnt_1 += 1
        if answers[i] == stu_2[(i%8)]:
            cnt_2 += 1
        if answers[i] == stu_3[(i%10)]:
            cnt_3 += 1
    
    cnt_total = [cnt_1, cnt_2, cnt_3]
    res = []
    m = max(cnt_total)
    for i in range(3):
        if m == cnt_total[i]:
            res.append(i+1)

    return res