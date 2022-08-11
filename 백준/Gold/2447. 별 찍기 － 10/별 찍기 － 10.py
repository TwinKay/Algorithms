n=int(input())
a=n
array = [["*" for col in range(n)] for row in range(n)]

def counting_star(n):
    if n == 1:
        
        for i in array :
            for j in i:
                print(j,end="")
            print()
        return
    
    
    else:
        
        for k in range(int(a/n)):
            for l in range(int(a/n)):
                for i in range(int(n/3)):
                    for j in range(int(n/3)):
                        array[int(n/3)+i+int(n)*l][int(n/3)+j+int(n)*k] = ' '

        n = n/3
        counting_star(n)
    

counting_star(n)