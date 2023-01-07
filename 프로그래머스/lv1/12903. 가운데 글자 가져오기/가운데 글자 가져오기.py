def solution(s):
    if len(s) % 2 == 1:
        ans = s[(len(s)-1)//2]
    else:
        ans = s[(len(s)-1)//2:((len(s)-1)//2)+2]
    return ans