def solution(s):
    l = 0 ; r = 0
    ans = True
    for i in s:
        if i == '(':
            l += 1
        else:
            r += 1
        if l < r:
            ans = False
            break
    if l != r:
        ans = False
        
    return ans