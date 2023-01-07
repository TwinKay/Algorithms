def solution(left, right):
    ans = 0
    for i in range(left, right+1):
        if (i**(1/2))%1 == 0:
            ans -= i
        else:
            ans += i
    return ans