n = int(input())

for i in range(200):
    globals()['list_' + str(i + 1)] = []

for i in range(n):
    a,b = input().split()

    globals()['list_' + a].append(b)

for i in range(200):
    if globals()['list_' + str(i + 1)] != []:
        for j in globals()['list_' + str(i + 1)]:
            print(i+1, j)