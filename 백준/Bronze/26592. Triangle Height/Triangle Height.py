n = int(input())
for _ in range(n):
    area, base = map(float, input().split())
    height = (2 * area) / base
    print(f"The height of the triangle is {height:.2f} units")