A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())

for t in [P, M, N]:
    cnt = 0

    x = t % (A + B)
    if x != 0 and x <= A:
        cnt += 1

    x = t % (C + D)
    if x != 0 and x <= C:
        cnt += 1

    print(cnt)