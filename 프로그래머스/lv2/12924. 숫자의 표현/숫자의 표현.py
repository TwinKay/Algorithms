def solution(n):
    cnt = 0
    for i in range(1,n):
        for j in range(i+1,n):
            if ((i+j)/2)*(j-i+1) == n:
                cnt += 1
                break
            elif ((i+j)/2)*(j-i+1) > n:
                break
    return cnt+1