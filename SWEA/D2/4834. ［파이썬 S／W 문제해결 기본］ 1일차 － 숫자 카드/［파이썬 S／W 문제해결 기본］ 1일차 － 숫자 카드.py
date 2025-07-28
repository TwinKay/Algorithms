T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, list(input())))

    dic = dict()
    for a in arr:
        if a in dic.keys():
            dic[a] += 1
        else:
            dic[a] = 1

    arr_sort = []
    for key in dic.keys():
        arr_sort.append([key,dic[key]])

    arr_sort = sorted(arr_sort, key=lambda x: (-x[1],-x[0]))
    print(f'#{t} {arr_sort[0][0]} {arr_sort[0][1]}')