n = int(input())
max_area = 0

for _ in range(n):
    h, w = map(int, input().split())
    area = h * w
    if area > max_area:
        max_area = area

print(max_area)