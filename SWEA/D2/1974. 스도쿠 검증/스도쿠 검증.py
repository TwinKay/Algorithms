'''
유형: 구현
아이디어:
    set 사용해서 단순하게 구해보기
'''

prt = []

def isRight():
    for i in range(9):
        if len(set(graph[i])) != 9:
            return False

    for i in range(9):
        if len(set(list(map(list, zip(*graph)))[i])) != 9:
            return False

    for i in range(0,9,3):
        for j in range(0,9,3):
            st = set()
            for k in range(3):
                for l in range(3):
                    st.add(graph[i+k][j+l])
            if len(st) != 9:
                return False

    return True


T = int(input())
for t in range(1,T+1):
    graph = []
    for _ in range(9):
        graph.append(list(map(int, input().split())))
    if isRight():
        prt.append(f"#{t} 1")
    else:
        prt.append(f"#{t} 0")
print("\n".join(prt))