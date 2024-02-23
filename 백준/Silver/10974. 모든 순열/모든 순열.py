import sys
from itertools import permutations

n = int(sys.stdin.readline())

arr = list(range(1,n+1))
l =list(permutations(arr,n))
for i in l:
    print(' '.join(list(map(str,i))))