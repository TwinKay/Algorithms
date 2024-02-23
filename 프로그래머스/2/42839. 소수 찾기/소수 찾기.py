from itertools import permutations
import math

def solution(numbers):
    nums = []
    for i in range(1,len(numbers)+1):
        nums.extend(list(permutations(numbers,i)))

    perm = set()
    for i in nums:
        a = ''.join(i)
        perm.add(int(a))
    perm = list(perm)
    
    def prime(x):
        if x==0 or x==1:
            return False
        for i in range(2,int(math.sqrt(x)+1)):
            if x % i == 0:
                return False
        return True
    
    res = 0
    for i in perm:
        if prime(i):
            res += 1

    return res