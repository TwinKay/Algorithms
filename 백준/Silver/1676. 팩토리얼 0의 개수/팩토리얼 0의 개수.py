n = int(input())
a = 1
for i in range(n):
    a = a*(i+1)

a = str(a)

t = 0
if a[len(a)-1] == str(0):
    t += 1

for i in range(len(a)-1):
    
    if a[len(a)-i-2] != str(0):
        break
        
    else:
        t += 1
    
print(t)