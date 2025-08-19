import sys
import math

def get_dist(x,y,z):
    return math.sqrt((cx-x)**2 + (cy-y)**2 + (cz-z)**2)

def find_max_dist():
    max_dist = -1
    max_idx = -1
    for i in range(N):
        dot = dots[i]
        dist = get_dist(dot[0],dot[1],dot[2])
        if dist > max_dist:
            max_dist = dist
            max_idx = i
    return max_idx
while True:
    N = int(sys.stdin.readline())
    if N==0:
        break
    dots = []
    for _ in range(N):
        dots.append(list(map(float, sys.stdin.readline().split())))

    cx,cy,cz = 0,0,0
    for dot in dots:
        cx+=dot[0]; cy+=dot[1]; cz+=dot[2]

    weight = 0.1
    cx/=N; cy/=N; cz/=N
    for _ in range(10000):
        max_dist_idx = find_max_dist()
        max_dist_dot = dots[max_dist_idx]
        cx += (max_dist_dot[0]-cx)*weight
        cy += (max_dist_dot[1]-cy)*weight
        cz += (max_dist_dot[2]-cz)*weight

        weight *= 0.99

    dot_idx = find_max_dist()
    fx,fy,fz = dots[dot_idx]
    r = get_dist(fx,fy,fz)
    print(f'{r:.5f}')