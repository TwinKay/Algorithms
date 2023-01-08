def solution(n):
    answer = ''
    while n>0:
        re = n%3
        n = n//3
        answer+=str(re)

    return int(answer, 3)