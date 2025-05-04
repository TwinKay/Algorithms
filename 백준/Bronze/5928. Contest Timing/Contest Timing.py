import sys

D, H, M = map(int, sys.stdin.readline().split())
minutes = (D - 11) * 24 * 60 + (H - 11) * 60 + (M - 11)
if minutes < 0:
    minutes = -1

print(minutes)