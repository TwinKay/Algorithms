S = input().strip()
target = "SciComLove"

diff_count = sum(1 for a, b in zip(S, target) if a != b)
print(diff_count)