L = []

for i in range(10):
    L.append(int(input())%42)

L = list(set(L))
print(len(L))