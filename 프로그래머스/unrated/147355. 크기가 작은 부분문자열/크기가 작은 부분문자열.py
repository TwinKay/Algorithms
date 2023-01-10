def solution(t, p):
    
    total = []
    for i in range(len(t)-len(p)+1):
        total.append(int(t[i:i+len(p)]))
    print(total)
    
    cnt = 0
    for i in total:
        if i <= int(p):
            cnt += 1
    
    return cnt