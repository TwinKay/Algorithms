'''
미리 만들고 쿼리에서는 출력만
'''
prt = []

pas = [[1]]
for i in range(1,10):
    pas.append([])
    for j in range(i+1):
        if j-1>=0 and j<i:
            pas[i].append(pas[i-1][j-1]+pas[i-1][j])
        elif j-1>=0:
            pas[i].append(pas[i-1][j-1])
        else:
            pas[i].append(pas[i-1][j])

T = int(input())
for t in range(1,T+1):
    N = int(input())
    print(f"#{t}")
    for i in range(N):
        print(*pas[i])
