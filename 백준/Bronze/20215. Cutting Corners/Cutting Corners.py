import math
import sys

w, h = map(int, sys.stdin.readline().split())

rect_cut = w + h
diag_cut = math.sqrt(w * w + h * h)
extra = rect_cut - diag_cut
print(extra)
