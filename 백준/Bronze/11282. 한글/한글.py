import sys

n = int(sys.stdin.readline())
base = 0xAC00
code_point = base + n - 1
print(chr(code_point))
