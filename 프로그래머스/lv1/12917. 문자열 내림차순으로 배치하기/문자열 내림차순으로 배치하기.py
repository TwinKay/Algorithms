def solution(s):
    answer = ''
    up = []
    lo = []
    for i in s:
        if i.isupper() == True:
            up.append(i)
        else:
            lo.append(i)
    up.sort(reverse = True)
    lo.sort(reverse = True)
    
    return ''.join(lo)+''.join(up)