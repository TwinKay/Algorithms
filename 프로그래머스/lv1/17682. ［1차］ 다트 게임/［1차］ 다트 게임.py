def solution(dartResult):
    res = []
    score = ['0','1','2','3','4','5','6','7','8','9']
    bonus = ['S','D','T']
    jump = False
    for n,i in enumerate(dartResult):
        if jump:
            jump = False
            pass
        elif i == '1' and dartResult[n+1] == '0':
            print("!!")
            temp = 10
            jump = True
        elif i in score:
            temp = int(i)
        elif i in bonus:
            if i == 'D':
                temp = temp**2
            elif i == 'T':
                temp = temp**3
            res.append(temp)
        elif i == '*':
            res[-1] = res[-1]*2
            if len(res) >= 2:
                res[-2] = res[-2]*2
        elif i == '#':
            res[-1] = res[-1]*(-1)
        
    return sum(res)