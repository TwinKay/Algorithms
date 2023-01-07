def solution(n):
    ans = 0
    
    for i in range(1,n+1):
        if n/i % 1 == 0:
            ans += (i+n/i)
    ans /= 2
    return ans