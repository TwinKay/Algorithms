s = input().strip()
i = 0
res = ''

while i < len(s):
    res += s[i]
    step = ord(s[i]) - ord('A') + 1
    i += step

print(res)