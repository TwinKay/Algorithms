import sys

n = int(sys.stdin.readline())

stairs = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

result = []

if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0]+stairs[1])
else:
    result.append(stairs[0])
    result.append(stairs[0]+stairs[1])
    result.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))
    for i in range(3,n):
        result.append(max(result[i-2]+stairs[i], result[i-3]+stairs[i-1]+stairs[i]))

    print(result.pop())