def solution(strings, n):
    strings.sort()
    s = []
    for i in range(len(strings)):
        s.append([strings[i],i])

    total = []
    for _ in range(26):
        total.append([])

    for a,b in s:
        total[ord(a[n])-97].append(b)

    for i in total:
        i.sort()

    res = []
    for i in total:
        for j in i:
            res.append(s[j][0])

    return res