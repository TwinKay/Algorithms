import sys

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def change_alpa(alpa):
    val = ord(alpa)-ord('a')+1
    if val < 1:
        val += 58
    return val

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append([])
total_length = 0
input_map = []
for i in range(N):
    input_map.append(list(sys.stdin.readline().rstrip()))

lst = []
for i in range(N):
    for j in range(N):
        if input_map[i][j] != '0':
            w = change_alpa(input_map[i][j])
            total_length += w
            lst.append([w,j,i])
            lst.append([w,i,j])

parent = []
for i in range(N):
    parent.append(i)

lst.sort()
use_length = 0
for next_info in lst:
    w, a,b = next_info
    if find(a) != find(b):
        use_length += w
        union(a, b)

s = set()
for p in parent:
    s.add(find(p))

if len(s) == 1:
    print(total_length-use_length)
else:
    print(-1)