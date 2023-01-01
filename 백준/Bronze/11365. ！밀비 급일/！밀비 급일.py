import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == 'END':
        break
    else:
        print(s[::-1])