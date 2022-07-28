n = int(input())

for k in range(n):
    a = input()
    a = a.split("X")
    
    L = []

    for i in a:
        total = 0
        for j in range(len(i)):
            total = total+j+1

        L.append(total)
        result = sum(L)

    print(result)