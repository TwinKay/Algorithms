def solution(nums):
    cnt = 0
    for i in nums:
        for j in nums:
            for k in nums:
                if i!=j and j!=k and i!=k:
                    a = i+j+k
                    for n in range(2,int(a**(1/2)+1)):
                        check = True
                        if a%n == 0:
                            check = False
                            break
                    if check:
                        cnt += 1


    return cnt//6