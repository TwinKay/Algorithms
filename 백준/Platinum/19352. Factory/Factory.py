import sys
import math

def get_dist(x,y):
    return math.sqrt((cx-x)**2 + (cy-y)**2)

def find_vector():
    sm_x,sm_y = 0.0,0.0
    sm_w = 0.0
    for dot in dots:
        dist = get_dist(dot[0],dot[1])
        if dist == 0.0:
            return
        w = 1.0 / dist

        sm_x += dot[0] * w
        sm_y += dot[1] * w
        sm_w += w
    return [sm_x/sm_w, sm_y/sm_w]
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dots = []
    for _ in range(N):
        dots.append(list(map(float, sys.stdin.readline().split())))

    cx,cy = 0.0,0.0
    for dot in dots:
        cx+=dot[0]; cy+=dot[1]
    cx/=N; cy/=N

    lr = 0.1
    gamma = 0.999
    for _ in range(10000):
        vec = find_vector()
        if not vec:
            break
        vx, vy = vec
        cx += (vx-cx)*lr
        cy += (vy-cy)*lr

        lr *= gamma

    print(f'{cx:.6f} {cy:.6f}')