n = int(input())
for j in range(n):
    case = input().split()
    case = list(map(int, case))
    N_stu = case[0]
    score_L = case[1:]
    aver = sum(score_L)/N_stu
    Pass = []
    for i in score_L:
        if i>aver:
            Pass.append(i)

    ratio = len(Pass)/N_stu*100
    ratio = round(ratio, 3)
    print(str('{:.3f}'.format(ratio))+"%")