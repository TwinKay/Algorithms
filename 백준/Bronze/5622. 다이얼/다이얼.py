alpha = ["A","B","C","D","E","F","G","H",'I',"J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
L = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9,9,9]

s = list(input())

dic = {}
for i in alpha:
    dic[i]=L[alpha.index(i)]+1

total = 0
for i in s:
    total += dic[i]
    
print(total)