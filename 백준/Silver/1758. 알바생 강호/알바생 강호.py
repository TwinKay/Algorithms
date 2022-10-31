import sys

n = int(sys.stdin.readline())
line = []
for _ in range(n):
    line.append(int(sys.stdin.readline()))
line.sort(reverse=True)

result = []
for j,i in enumerate(line):
    if i-j >0:
        result.append(i-j)
        
print(sum(result))