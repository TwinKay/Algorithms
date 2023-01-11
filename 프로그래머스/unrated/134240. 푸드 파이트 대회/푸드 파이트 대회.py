def solution(food):
    res = ''
    for n, i in enumerate(food):
        if n == 0:
            pass
        if i%2 != 0:
            i-=1
        res += str(n)*(i//2)
    res = res + '0' + res[::-1]

    return res