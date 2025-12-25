N, W, H = map(int, input().split())

max_len = W * W + H * H

for _ in range(N):
    L = int(input())
    if L * L <= max_len:
        print("DA")
    else:
        print("NE")