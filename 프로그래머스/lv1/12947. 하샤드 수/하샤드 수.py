def solution(x):
    a = sum(list(map(int, list(str(x)))))
    
    return x%a == 0