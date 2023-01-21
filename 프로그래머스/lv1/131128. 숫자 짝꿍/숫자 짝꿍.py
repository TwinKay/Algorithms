def solution(X, Y):
    dic_x = {}
    dic_y = {}
    for i in range(10):
        dic_x[str(i)] = 0
        dic_y[str(i)] = 0
        
    for i in X:
        dic_x[i] += 1
    for i in Y:
        dic_y[i] += 1

    res = ''
    d_x = list(dic_x.values())
    d_y = list(dic_y.values())
    for i in range(9,-1,-1):
        m = min(d_x[i], d_y[i])
        if m>=1 and res == '' and i==0:
            return '0'
        
        if m != 0:
            res+=str(i)*m
    
    if res == '':
        return '-1'
    else:
        return res
