import sys

def perm(num,res_arr):
    if len(res_arr) == M:
        print(*res_arr)
        return
    for i in range(1,num+1):
        res_arr.append(i)
        perm(num,res_arr)
        res_arr.pop()


N,M = map(int, sys.stdin.readline().split())

perm(N,[])