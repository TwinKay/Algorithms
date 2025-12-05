n = int(input())
files = []
for _ in range(n):
    files.append(input())
    
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    for i in range(l-1, r):
        print(files[i])