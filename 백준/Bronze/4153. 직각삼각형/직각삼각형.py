while True:
    basket = list(map(int,input().split()))
    basket.sort()
    if basket[0] == 0 and basket[1] == 0 and basket[2] == 0 :
        break
    else:
        if basket[0]**2 + basket[1]**2 == basket[2]**2:
            print('right')
        else:
            print('wrong')