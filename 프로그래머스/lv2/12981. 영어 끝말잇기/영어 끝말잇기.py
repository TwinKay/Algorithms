def solution(n, words):
    done = []
    for num,i in enumerate(words):
        if len(i) == 1:
            break
        elif num == 0:
            done.append(i)
        else:
            if i in done:
                break
            elif done[-1][-1] != i[0]:
                break
            else:
                done.append(i)
    
    if len(done) != len(words):
        if (len(done)+1) % n == 0:
            return [n, ((len(done))+1)//n]
        else:
            return[(len(done)+1) % n, (((len(done))+1)//n)+1]
        
        
        
    else:
        return [0,0]
    
    
    
    
    
    
    
    answer = []
    return answer