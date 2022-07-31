n = int(input())

if n%5 == 1:
    if n == 1:
        print(-1)
    else:
        print(n//5+1)
elif n%5 == 2:
    if n ==2 or n ==7:
        print(-1)
    else:
        print(n//5+2)
elif n%5 ==3:
    print(n//5+1)
elif n%5 ==4:
    if n==4:
        print(-1)
    else:
        print(n//5+2)
else:
    print(n//5)