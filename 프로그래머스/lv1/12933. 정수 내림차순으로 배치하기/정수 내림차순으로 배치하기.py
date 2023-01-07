def solution(n):
    ans = list(str(n))
    ans.sort(reverse = True)
    ans = ''.join(ans)
    return int(ans)