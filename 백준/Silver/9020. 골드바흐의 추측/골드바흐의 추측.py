import sys

t = int(sys.stdin.readline())

for k in range(t):
    n = int(sys.stdin.readline())

    torf_List = [True]*(n+1)
    torf_List[0] = False
    torf_List[1] = False

    for i in range(2,int((n**0.5))+1):
        if torf_List[i] == True:
            for j in range(i*2, n+1, i):
                torf_List[j] = False

    a = n//2
    while True:
        if torf_List[a] == True  and  torf_List[n-a] == True:
            print(str(a)+' '+str(n-a))
            break

        else:
            a = a-1