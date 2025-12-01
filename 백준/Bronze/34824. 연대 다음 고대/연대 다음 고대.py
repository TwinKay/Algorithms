N = int(input())

yonsei_rank = -1
korea_rank = -1

for i in range(N):
    name = input().strip()
    if name == "yonsei":
        yonsei_rank = i
    elif name == "korea":
        korea_rank = i

if yonsei_rank < korea_rank:
    print("Yonsei Won!")
else:
    print("Yonsei Lost...")