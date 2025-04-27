import sys

n = int(sys.stdin.readline())
directions = sys.stdin.readline().strip()

cnt = {'N': 0, 'S': 0, 'E': 0, 'W': 0}

for d in directions:
    cnt[d] += 1
vertical_steps = abs(cnt['N'] - cnt['S'])
horizontal_steps = abs(cnt['E'] - cnt['W'])

print(vertical_steps + horizontal_steps)

