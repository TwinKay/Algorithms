import sys

P = int(sys.stdin.readline())
for _ in range(P):
    temp = list(map(int, sys.stdin.readline().split()))
    t = temp[0]
    arr = temp[1:]

    line = []
    line.append(arr[0])

    cnt = 0
    for i in range(1,len(arr)):
        line.append(arr[i])
        idx = len(line) - 1
        for _ in range(len(line)-1):
            if line[idx-1] > line[idx]:
                line[idx], line[idx-1] = line[idx-1], line[idx]
                cnt += 1
                idx -= 1
            else:
                break
    print(t, cnt)