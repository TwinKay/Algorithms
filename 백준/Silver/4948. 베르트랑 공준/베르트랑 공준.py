import sys

while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break
        
    else:
        torf_List = [True]*(2*n+1)
        torf_List[0] = False
        torf_List[1] = False

        for i in range(2,int(((2*n)**0.5))+1):
            if torf_List[i] == True:
                for j in range(i*2, 2*n+1, i):
                    torf_List[j] = False

        torf_List = torf_List[n+1:]
        print(torf_List.count(True))