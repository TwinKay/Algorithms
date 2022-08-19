k = int(input())

total =[]
for _ in range(6):
    a,b = map(int, input().split())
    total.append([a,b])

while True:
    if total[0][0] == total[2][0] and total[1][0] == total[3][0]:
        break
        
    else:
        total = [total[1],total[2],total[3],total[4],total[5],total[0]]

print((total[4][1]*total[5][1] - total[1][1]*total[2][1])*k)