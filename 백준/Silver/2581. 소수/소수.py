x = int(input())
y = int(input())

c = []
s = []

for k in range(y-x+1):
    c.append(x+k)

    
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
            s.append(a)


if s == []:
    print(-1)
    
else:
    print(sum(s))
    print(min(s))