import sys
import math

def get_dist(x,y,z):
    return math.sqrt((cx-x)**2 + (cy-y)**2 + (cz-z)**2)

def find_vector():
    sm_x,sm_y,sm_z = 0.0,0.0,0.0
    sm_w = 0.0
    for dot in dots:
        dist = get_dist(dot[0],dot[1],dot[2])
        if dist == 0.0:
            return
        w = 1.0 / dist

        sm_x += dot[0] * w
        sm_y += dot[1] * w
        sm_z += dot[2] * w
        sm_w += w
    return [sm_x/sm_w, sm_y/sm_w, sm_z/sm_w]

N = 3
dots = []
for _ in range(N):
    dots.append(list(map(float, sys.stdin.readline().split())))

cx,cy,cz = 0.0,0.0,0.0
for dot in dots:
    cx+=dot[0]; cy+=dot[1]; cz+=dot[2]
cx/=N; cy/=N; cz/=N

weight = 0.1
for _ in range(10000):
    vec = find_vector()
    if not vec:
        break
    vx, vy, vz = vec
    cx += (vx-cx)*weight
    cy += (vy-cy)*weight
    cz += (vz-cz)*weight

    weight *= 0.999

total_dist = 0.0
for dot in dots:
    total_dist += get_dist(dot[0],dot[1],dot[2])
print(f'{total_dist:.6f}')