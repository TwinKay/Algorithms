'''
아이디어:
입력을 String 자체롤 받은 후, nPr 수행하며 join후에 set에 넣기
'''
import sys

def back_tracking(n,cand):
    if n == K: # 기저
        s.add("".join(cand))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            cand.append(arr[i])
            back_tracking(n+1,cand)
            visited[i] = False
            cand.pop()


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

s = set() # 정수 담을 set
visited = [False]*N
back_tracking(0,[]) # n, 조합 담을 arr
print(len(s))
