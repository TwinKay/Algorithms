N = int(input())
a_win = 0
b_win = 0

for _ in range(N):
    A, B = map(int, input().split())
    if A > B:
        a_win += 1
    elif A < B:
        b_win += 1

print(a_win, b_win)