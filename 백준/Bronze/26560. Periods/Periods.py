n = int(input())
for _ in range(n):
    line = input().rstrip()
    if not line.endswith('.'):
        line += '.'
    print(line)
