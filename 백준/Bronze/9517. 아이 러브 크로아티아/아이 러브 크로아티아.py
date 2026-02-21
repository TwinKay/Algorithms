k = int(input())
n = int(input())

time = 0
holder = k

for _ in range(n):
    t, z = input().split()
    t = int(t)

    time += t
    if time >= 210:
        print(holder)
        break

    if z == 'T':
        holder += 1
        if holder == 9:
            holder = 1