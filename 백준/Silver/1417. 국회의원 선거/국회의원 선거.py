import sys


def is_win():
    for i in range(1,N):
        if votes[i] >= votes[0]:
            return False

    return True


def steal():
    max_val = max(votes)
    for i in range(1,N):
        if votes[i] == max_val:
            votes[i] -= 1
            votes[0] += 1
            return


N = int(sys.stdin.readline())
votes = []
for _ in range(N):
    votes.append(int(sys.stdin.readline()))

cnt = 0
while True:
    if is_win():
        break
    steal()
    cnt += 1

print(cnt)