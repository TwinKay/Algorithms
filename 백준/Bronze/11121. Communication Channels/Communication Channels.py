T = int(input())

for _ in range(T):
    original, received = input().split()
    if original == received:
        print("OK")
    else:
        print("ERROR")
