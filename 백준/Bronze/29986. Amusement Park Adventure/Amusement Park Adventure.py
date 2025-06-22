N, H = map(int, input().split())
ride_limits = list(map(int, input().split()))

count = sum(1 for limit in ride_limits if H >= limit)
print(count)