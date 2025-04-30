import sys

for _ in range(3):
    data = sys.stdin.readline().split()
    h1 = int(data[0])
    m1 = int(data[1])
    s1 = int(data[2])
    h2 = int(data[3])
    m2 = int(data[4])
    s2 = int(data[5])

    s = s2 - s1
    if s < 0:
        s += 60
        m2 -= 1

    m = m2 - m1
    if m < 0:
        m += 60
        h2 -= 1

    h = h2 - h1

    print(h, m, s)
