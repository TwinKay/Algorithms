def solution(s):
    try:
        a = list(map(int, list(s)))
        if len(s) == 4 or len(s) == 6:
            ans = True
        else:
            ans = False
    except:
        ans = False
        
    return ans