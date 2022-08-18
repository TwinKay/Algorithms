n = int(input())

for i in range(50):
    globals()['list_' + str(i + 1)] = []

for i in range(n):
    a = input()
    globals()['list_' + str(len(a))].append(a)

for i in range(50):
    globals()['list_' + str(i + 1)] = list(set(globals()['list_' + str(i + 1)]))
    globals()['list_' + str(i + 1)].sort()


for i in range(50):
    if globals()['list_' + str(i + 1)] != []:
        for j in globals()['list_' + str(i + 1)]:
            print(j)