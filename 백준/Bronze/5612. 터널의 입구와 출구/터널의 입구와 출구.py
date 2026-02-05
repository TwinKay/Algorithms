import sys

n = int(input())
cur = int(input())

max_cars = cur

for _ in range(n):
    in_cars, out_cars = map(int, input().split())
    cur += in_cars
    cur -= out_cars

    if cur < 0:
        print(0)
        sys.exit(0)

    max_cars = max(max_cars, cur)

print(max_cars)