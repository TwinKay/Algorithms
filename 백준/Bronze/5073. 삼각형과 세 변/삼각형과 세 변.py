import sys

while True:
    total = list(map(int, sys.stdin.readline().split()))
    total.sort()
    a,b,c = total[0],total[1],total[2]

    if a==0 and b==0 and c==0:
        break
    else:
        if a+b<=c:
            print('Invalid')
        elif a == b and b ==c and c== a:
            print('Equilateral')
        elif a == b or b ==c or c == a:
            print('Isosceles')
        else:
            print('Scalene')