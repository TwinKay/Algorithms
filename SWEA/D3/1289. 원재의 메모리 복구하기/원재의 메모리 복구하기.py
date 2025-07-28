T = int(input())
for t in range(1,T+1):
    bits = list(map(int,list(input().rstrip())))
    cnt = 0
    for i in range(len(bits)):
        if bits[i]==1:
            for j in range(i,len(bits)):
                if bits[j] == 1:
                    bits[j] = 0
                else:
                    bits[j] = 1
            cnt += 1

    print(f'#{t} {cnt}')