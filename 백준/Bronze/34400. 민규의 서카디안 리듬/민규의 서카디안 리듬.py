T = int(input())
for _ in range(T):
    t = int(input())
    time = (t + 0.5) % 25
    if time < 17:
        print("ONLINE")
    else:
        print("OFFLINE")