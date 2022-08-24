import sys

for _ in range(int(sys.stdin.readline())):

    x_1, y_1, x_2, y_2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())

    t = 0
    for _ in range(n):
        c_x, c_y, r = map(int, sys.stdin.readline().split())

        d_x = ((x_1-c_x)**2 + (y_1-c_y)**2)**0.5
        d_y = ((x_2-c_x)**2 + (y_2-c_y)**2)**0.5

        if d_x < r and d_y > r:
            t += 1
        elif d_x > r and d_y < r:
            t += 1

    print(t)
    
# 원 안에 두 점 중 하나만 포함될 때!