n = int(input())
c = list(map(int,input().split()))
t = 0
L_all = []

for j in range(1000):
    L_all.append(j+1)


for a in c:
    if a == 1 :
        pass
    
    else:
        L = []

        for i in range(a-2):
            if a/(i+2)%1 == 0 :
                L.append(a)
        if L == []:
            t = t+1
print(t)