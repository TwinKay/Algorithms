t = int(input())
h = 0

for n in range(t+1):
    n = str(n)
    L = list(n)
    L = list(map(int, L))


    if len(L) == 1 or len(L) == 2 :
        h += 1

    else:
        if L[1]-L[0] == L[2]-L[1]:
            h += 1

        else:
            pass

print(h-1)