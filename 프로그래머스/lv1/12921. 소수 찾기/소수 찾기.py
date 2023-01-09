def solution(n):
    
    res = []
    for i in range(2,n+1):
        check = True
        for j in range(2,int(i**(1/2))+1):
            if i%j == 0:
                check = False
                break
        if check:
            res.append(i)

    return len(res)