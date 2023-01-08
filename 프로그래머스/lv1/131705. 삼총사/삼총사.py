def solution(number):
    res = 0
    for i in range(len(number)):
        for j in range(len(number)):
            for k in range(len(number)):
                if i != j and j != k and i!= k:
                    if number[i]+number[j]+number[k] == 0:
                        res += 1
    
    return res//6