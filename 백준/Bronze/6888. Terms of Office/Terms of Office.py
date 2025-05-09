import sys

data = sys.stdin.read().split()
X, Y = map(int, data)
for year in range(X, Y + 1, 60):
    print(f"All positions change in year {year}")