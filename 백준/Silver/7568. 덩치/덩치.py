n = int(input())
dungchi = []
result = []

for i in range(n):
    a,b = map(int,input().split())
    dungchi.append([a,b])


for i in dungchi:
    t = 1
    for j in dungchi:
        
        if i[0]<j[0] and i[1]<j[1]:
            t += 1
    result.append(t)
    
for i,j in enumerate(result):
    if i == n-1:
        print(j)
    
    else:
        print(j, end=' ')