a=1
L_total = []
self_n = 0
while a<10000:
    a = str(a)
    L_a = list(map(int, list(a)))
    sum_a = sum(L_a)
    self_n = int(a)+sum_a
    L_total.append(self_n)
    
    a = int(a)
    a += 1
    
L_total = list(set(L_total))

result = []
for i in range(10000):
    if i+1 not in L_total:
        result.append(i+1)

for j in result:
    print(j)