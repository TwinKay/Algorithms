a,b,c,d,e = map(int,input().split())

a = a**2
b = b**2
c = c**2
d = d**2
e = e**2

result = a+b+c+d+e
print(result%10)