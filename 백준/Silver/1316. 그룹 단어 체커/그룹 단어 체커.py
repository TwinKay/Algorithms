case = int(input())
c = 0
for i in range(case):
    s = input()
    i=0


    while True:
        try:
            if s[i] == s[i+1]:
                s = s[:i+1]+s[i+2:]

            else:
                i=i+1

        except:
            break


    alpha = ["a","b","c","d","e","f","g","h",'i',"j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    L = []
    for i in range(len(alpha)):
        a = s.count(alpha[i])
        L.append(a)
    L = list(set(L))

    for i in L:
        if i ==0 or i==1:
            pass
        else:
            c = c+1
            break
print(case-c)