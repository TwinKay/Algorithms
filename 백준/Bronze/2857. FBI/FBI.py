ans = []

for i in range(1, 6):
    s = input().strip()
    if "FBI" in s:
        ans.append(i)

if ans:
    print(" ".join(map(str, ans)))
else:
    print("HE GOT AWAY!")