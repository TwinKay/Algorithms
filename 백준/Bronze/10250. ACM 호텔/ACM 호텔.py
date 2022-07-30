a = int(input())
for i in range(a):
    h, w, n = map(int, input().split())
    x = n%h
    y = (n//h)+1

    if x == 0:
        if y <= 10:
            print(str(h)+str("0")+str((n-1)//(h)+1))

        else:
            print(str(h)+str((n-1)//(h)+1))  



    elif y < 10:
        print(str(x)+str("0")+str(y))

    else:
        print(str(x)+str(y))