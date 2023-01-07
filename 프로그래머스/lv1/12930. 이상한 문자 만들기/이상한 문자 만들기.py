def solution(s):
    res = []
    up = True
    for i in s:
        if i == ' ':
            up = True
            res.append(' ')
        
        elif up == True:
            up = False
            res.append(i.upper())
        else:
            up = True
            res.append(i.lower())

    return ''.join(res)