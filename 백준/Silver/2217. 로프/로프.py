import sys

n = int(sys.stdin.readline())
rope = []
for _ in range(n):
    rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True)

result = []
for j,i in enumerate(rope):
    result.append(i*(j+1))
print(max(result))
