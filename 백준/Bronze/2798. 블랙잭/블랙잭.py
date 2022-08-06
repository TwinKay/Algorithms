n,m = map(int,input().split())
card_list = list(map(int,input().split()))
result = []

for i in card_list:
    for j in card_list:
        for k in card_list:
            if i == j or j == k or i ==k:
                pass
            else:
                result.append(i+j+k)
                
result = list(set(result))
result_2 = []

for i in result:
    if i <= m:
        result_2.append(i)

print(max(result_2))