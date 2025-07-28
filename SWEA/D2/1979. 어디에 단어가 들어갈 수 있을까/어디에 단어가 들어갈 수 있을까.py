'''
유형: 구현
주의사항:
    더 큰 공간 X -> 정확히 같은 크기로만 들어갈 수 있음
'''

prt = []

T = int(input())
for t in range(1,T+1):
    N,M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    cnt_arr = [0]*(N+1) # 흰 막대기 갯수 세기를 위한 배열 -> idx 0은 dummy

    for i in range(N):
        length = 0
        for j in range(N):
            if graph[i][j] == 1:
                length += 1
            else:
                cnt_arr[length] += 1
                length = 0

            if j==N-1: # 마지막에 남아있을 수 있음으로! -> graph를 검은색으로 둘러도 된다!
                cnt_arr[length] += 1

    for i in range(N):
        length = 0
        for j in range(N):
            if graph[j][i] == 1:
                length += 1
            else:
                cnt_arr[length] += 1
                length = 0

            if j==N-1:
                cnt_arr[length] += 1

    prt.append(f"#{t} {cnt_arr[M]}")

print("\n".join(prt))
