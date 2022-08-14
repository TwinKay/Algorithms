n = int(input())
total = []

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                total.append(int('666'+str(a)+str(b)+str(c)+str(d)))
                total.append(int(str(a)+'666'+str(b)+str(c)+str(d)))
                total.append(int(str(a)+str(b)+'666'+str(c)+str(d)))
                total.append(int(str(a)+str(b)+str(c)+'666'+str(d)))
                total.append(int(str(a)+str(b)+str(c)+str(d)+'666'))
        
total = list(set(total))
total.sort()
print(total[n-1])