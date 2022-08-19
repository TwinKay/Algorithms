for _ in range(int(input())):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    d = ((x_1-x_2)**2+(y_1-y_2)**2)**(0.5)

    if d == 0:
        if r_1 == r_2:
            print(-1)
        else:
            print(0)
    else:
        if d > r_1+r_2:
            print(0)
        elif ((r_1-r_2)**2)**(0.5) > d:
            print(0)
        elif d == r_1+r_2:
            print(1)
        elif ((r_1-r_2)**2)**(0.5) == d:
            print(1)
        else:
            print(2)