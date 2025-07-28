res = []

T = int(input())
for t in range(1,T+1):
    # 입력
    N,M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    max_val = 0
    for i in range(N-M+1): # 세로 이동 횟수
        for j in range(N-M+1): # 가로 이동 횟수
            sm = 0
            for k in range(M):  # 파리채 세로 크기 만큼
                for l in range(M): # 파리채 가로 크기 만큼
                    sm += arr[i+k][j+l]
            max_val = max(max_val,sm)

    res.append(f"#{t} {max_val}")
    
print("\n".join(res))