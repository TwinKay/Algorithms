def solution(n, arr1, arr2):
    graph = []
    arr1_2 = []
    arr2_2 = []
    
    for _ in range(n):
        graph.append([])

    for i in range(n):
        arr1_2.append(format(arr1[i], 'b'))
        arr2_2.append(format(arr2[i], 'b'))

    for i in range(n):
        arr1_2[i] = '0'*(n-len(arr1_2[i])) + ''.join(arr1_2[i])
        arr2_2[i] = '0'*(n-len(arr2_2[i])) + ''.join(arr2_2[i])

    for i in range(n):
        for j in range(n):
            if arr1_2[i][j] =='0' and arr2_2[i][j] =='0':
                graph[i].append(0)
            else:
                graph[i].append(1)

    res = []
    for i in graph:
        line = ''
        for j in i:
            if j == 1:
                line+='#'
            else:
                line+=' '
        res.append(line)

    return res