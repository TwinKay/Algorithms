T = int(input())
for _ in range(T):
    input()

    n_line = input()
    while n_line == "":
        n_line = input().strip()
    N = int(n_line)

    s = 0
    for _ in range(N):
        x = int(input())
        s = (s + x) % N

    print("YES" if s == 0 else "NO")