import sys

res_num = 0
res_idx = 0
for i in range(1,10):
    n = int(sys.stdin.readline())
    if n > res_num:
        res_num = n
        res_idx = i
        
print(res_num)
print(res_idx)