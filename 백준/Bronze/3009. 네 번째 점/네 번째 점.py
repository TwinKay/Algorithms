a,b = map(int, input().split())
c,d = map(int, input().split())
e,f = map(int, input().split())
list_x = [a,c,e]
list_y = [b,d,f]

for i in list_x:
    if list_x.count(i) == 1:
        print(i,end=' ')

for i in list_y:
    if list_y.count(i) == 1:
        print(i)