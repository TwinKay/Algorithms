import sys

n,k = map(int, sys.stdin.readline().split())
total = list(range(2,n+1))

t = 0
breaker = False
while True:
    if breaker == True:
        break
    else:
        a = total[0]
        for i in total:
            if i % a == 0:
                t += 1
                if t == k:
                    print(i)
                    breaker = True
                    break

                else:
                    total.remove(i)