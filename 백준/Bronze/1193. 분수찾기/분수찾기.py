n =int(input())
a = 0
i = 0

while n > a :
    i += 1
    a = a+i

x = i+n-a
y = i-x+1

if i % 2 == 1:
    x, y = y, x

print(str(x)+"/"+str(y))