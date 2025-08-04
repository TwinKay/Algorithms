'''
자식에서 부모로 찾아가는 과정으로 구하기
부모로 탐색해서 올라가는 path를 기록해두고
두 노드의 패스를 set에 합치면서 in == True가 나올 때까지 진행
'''

def recu(c,path): # 자식에서 부모 탐색
    path.append(c)
    if not parent_arr[c]:
        return path
    else:
        recu(parent_arr[c],path)
    return path

import sys
sys.setrecursionlimit(10**5)

T = int(sys.stdin.readline())
for t in range(1,T+1):
    N = int(sys.stdin.readline())
    parent_arr = [0]*(N+1)
    for _ in range(N-1):
        a,b = map(int, sys.stdin.readline().split())
        parent_arr[b] = a

    node_a,node_b = map(int, sys.stdin.readline().split())
    path1 = recu(node_a,[])
    path2 = recu(node_b,[])

    parent_set = set()
    for i in range(max(len(path1),len(path2))):
        if i < len(path1): # indexError 방지
            if path1[i] in parent_set:
                print(path1[i])
                break
            else:
                parent_set.add(path1[i])
        if i < len(path2): # indexError 방지
            if path2[i] in parent_set:
                print(path2[i])
                break
            else:
                parent_set.add(path2[i])