a = input().strip()
b = input().strip()

x1, y1 = ord(a[0]) - ord('a') + 1, int(a[1])
x2, y2 = ord(b[0]) - ord('a') + 1, int(b[1])

dx = abs(x1 - x2)
dy = abs(y1 - y2)

x, y = sorted([dx, dy])
print(x, y)
