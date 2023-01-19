def solution(s):
    l = list(map(int, s.split()))
    ans = str(min(l))+' '+str(max(l))
    return ans