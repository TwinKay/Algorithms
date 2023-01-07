def solution(a, b):
    if a > b:
        a,b = b,a
    
    if a == b:
        ans = a
    else:
        ans = sum(list(range(a,b+1)))
    
    return ans