import sys
x = int(sys.stdin.readline())

forward_moves = (x + 1) // 2
backward_moves = x // 2

result = forward_moves * 3 - backward_moves * 2
print(result)
