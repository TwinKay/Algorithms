a = int(input())
b = int(input())
c = int(input())

total = a*b*c
total = str(total)

for i in range(10):
    print(total.count(str(i)))