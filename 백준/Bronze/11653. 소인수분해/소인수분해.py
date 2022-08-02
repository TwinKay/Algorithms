n = int(input())
x = n
c = list(range(2,x+1))

for a in c:
    if n == 1 :
        break
    
    elif a == 1 :
        pass
    
    else:
        L = []

        for i in range(a-2):
            if a/(i+2)%1 == 0 :
                L.append(a)
                break
                
            else:
                break
                
        if L == []:
            while True:
                if n % a == 0:
                    n = n/a
                    print(a)
                    
                else:
                    break