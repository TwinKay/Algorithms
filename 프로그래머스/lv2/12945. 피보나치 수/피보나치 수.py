def solution(n):
    fibo = []
    for i in range(n+1):
        if i == 0:
            fibo.append(0)
        elif i == 1 or i == 2:
            fibo.append(1)
        else:
            fibo.append(fibo[-1]+fibo[-2])

    return fibo.pop()%1234567