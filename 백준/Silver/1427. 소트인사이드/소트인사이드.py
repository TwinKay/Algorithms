n = input()
sort_list = []
for i in range(len(n)):
    sort_list.append(int(n[i]))

sort_list.sort(reverse=True)

for i in sort_list:
    print(i,end='')