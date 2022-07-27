a,b = map(int, input().split())

c = input().split()
c = list(map(int,c))

for i in c:
    if i<b:
        print(i, end=" ")