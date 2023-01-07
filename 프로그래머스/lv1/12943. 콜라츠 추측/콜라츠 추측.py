def solution(num):
    cnt = 0
    
    while True:
        if cnt > 500:
            cnt = -1
            break
            
        elif num == 1:
            break
        
        elif num != 1:
            if num % 2 == 1:
                num = num*3+1
                cnt += 1
            else:
                num /= 2
                cnt += 1
    
    return cnt