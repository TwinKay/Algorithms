x, y = map(int,input().split())
c = list(range(x,y+1))

for a in c:
    if a == 1 :
        pass
    
    else:
        L = []

        for i in range(2, int(a**(1/2))+1):
            
            if a/i%1 == 0 :
                L.append(a)
                break

        if L == []:
            print(a)