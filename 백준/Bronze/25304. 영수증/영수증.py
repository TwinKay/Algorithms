ans = int(input())
result = 0
t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    c = a*b
    result = result + c
    
if ans == result:
    print("Yes")
else:
    print("No")