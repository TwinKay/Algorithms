import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    mbti = list(sys.stdin.readline().split())

    if n >= 48:
        print(0)
    else:
        min_dis = 100
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i > j > k:
                        l_1 = mbti[i]
                        l_2 = mbti[j]
                        l_3 = mbti[k]

                        s_1 = set(list(l_1)).union(list(l_2))
                        s_2 = set(list(l_1)).union(list(l_3))
                        s_3 = set(list(l_2)).union(list(l_3))
                        min_dis = min(min_dis, len(s_1)+len(s_2)+len(s_3)-12)
        print(min_dis)