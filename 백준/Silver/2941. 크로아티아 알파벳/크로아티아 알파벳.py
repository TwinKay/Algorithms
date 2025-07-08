import sys

s = sys.stdin.readline().rstrip()

res = 0
i = 0
while i < len(s):
    if i + 2 < len(s) and s[i:i+3] == "dz=":
        res += 1
        i += 3
    elif i + 1 < len(s) and s[i:i+2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
        res += 1
        i += 2
    else:
        res += 1
        i += 1

print(res)