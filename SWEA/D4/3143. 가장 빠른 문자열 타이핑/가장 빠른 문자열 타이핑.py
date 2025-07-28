'''
aaabc aa 같은 것 조심
'''
res = []

T = int(input())
for t in range(1,T+1):
    s, key = input().split()
    s = list(s); key = list(key)
    visited = [False]*len(s)
    cnt_keys = 0
    for i in range(len(s)-len(key)+1):
        if visited[i]:
            continue
        is_right = True
        for j in range(len(key)):
            if s[i+j] != key[j]:
                is_right = False
                break
        if is_right:
            for j in range(len(key)):
                visited[i+j] = True
            cnt_keys += 1
    for v in visited:
        if not v:
            cnt_keys += 1
    res.append(f'#{t} {cnt_keys}')
print("\n".join(res))

