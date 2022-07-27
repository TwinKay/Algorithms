n = int(input())
m = 100
t = 0
while True:
    
    if n==m:
        break

    else:

        
        if m == 100:
            m = n
        
            if m<10:
                m = m*11
                t = t+1

            else:
                m = m%10*10 + ((m//10)+(m%10))%10
                t = t+1
                
                
        else:
            
            if m<10:
                m = m*11
                t = t+1

            else:
                m = m%10*10 + ((m//10)+(m%10))%10
                t = t+1
        
print(t)