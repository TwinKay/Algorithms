import sys

depth = 0

for line in sys.stdin:
    parts = line.strip().split()
    if not parts:
        continue
    kind, x = parts[0], int(parts[1])
    if kind == "Stair":
        depth += x * 17
    elif kind == "Es":
        depth += x * 21

print(depth)