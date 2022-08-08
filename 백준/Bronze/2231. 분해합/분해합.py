n = input()
result = []

for i in range(int(n)):
    result.append(int(i+1)+sum(map(int,list(str(i+1)))))

if int(n) in result:
    print(result.index(int(n))+1)
else:
    print(0)