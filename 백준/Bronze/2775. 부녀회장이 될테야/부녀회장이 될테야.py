t = int(input())
for p in range(t):
    k = int(input())
    n = int(input())
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    if k == 1:
        a = sum(l[:n])
    else:
        for i in range(k-1):
            for j in range(14):

                l.append(sum(l[:j+1]))
            l = l[14:]
        a = sum(l[:n])
    print(a)