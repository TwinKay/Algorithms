alpha = ["A","B","C","D","E","F","G","H",'I',"J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

s = input()
s = s.upper()

L = list(s)

result = []

for i in alpha:
    a = L.count(i)
    result.append(a)
    
if result.count(max(result)) > 1:
    print("?")

else:
    n = result.index(max(result))
    print(alpha[n])