m,n = map(int, input().split())
board = []
for i in range(m):
    board.append(input())

result = []
for i in range(m-7):
    result.append(board[i:i+8])

c = 0
find_min = []
for o in range(2):
    for i in result:
        for j in range(n-7):
            for a,k in enumerate(i):
                
                if a%2 == o:
                    for l in range(8):
                        if k[j+l] != 'BWBWBWBW'[l]:
                            c += 1
                            
                else:
                     for l in range(8):
                        if k[j+l] != 'WBWBWBWB'[l]:
                            c += 1
            find_min.append(c)
            c = 0


print(min(find_min))