n = int(input())
after_L = []

L = input().split()
L = list(map(int, L))

M=max(L)

for i in L:
    after_L.append(i/M*100)
    
a = sum(after_L)/n

print(a)