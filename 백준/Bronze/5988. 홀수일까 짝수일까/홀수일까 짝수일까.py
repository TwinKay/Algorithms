n = int(input())

for _ in range(n):
    k = input().strip()
    if int(k[-1]) % 2 == 0:
        print("even")
    else:
        print("odd")