def solution(answers):
    supo_1 = [1,2,3,4,5]
    supo_2 = [2,1,2,3,2,4,2,5]
    supo_3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt = [0,0,0]
    for i in range(len(answers)):
        if supo_1[i%5] == answers[i]:
            cnt[0] += 1
        if supo_2[i%8] == answers[i]:
            cnt[1] += 1
        if supo_3[i%10] == answers[i]:
            cnt[2] += 1

    res = []
    for i in range(3):
        if cnt[i] == max(cnt):
            res.append(i+1)

    return res