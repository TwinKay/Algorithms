import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
arr = list()
for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

s = set()

def perm(res_arr,K,visited):
    if len(res_arr) == K:
        s.add(int("".join(res_arr)))
        return
    for i in range(N):
        if not visited[i]:
            res_arr.append(arr[i])
            visited[i] = True
            perm(res_arr,K,visited)
            visited[i] = False
            res_arr.pop()

perm([],K,[False]*N)

print(len(s))