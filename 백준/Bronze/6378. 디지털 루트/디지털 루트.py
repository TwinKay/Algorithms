import sys

for line in sys.stdin:
    n = line.strip()
    if not n:
        continue
    if n == "0":
        break

    s = 0
    for ch in n:
        s += ord(ch) - 48

    print(1 + (s - 1) % 9)