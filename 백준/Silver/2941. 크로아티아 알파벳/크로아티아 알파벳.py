L = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
c = 0

s = input()

while True:
    if len(s) == 0:
        break
        
    else:
        
        if s[0:2] in L:
            c = c+1
            s = s[2:]
        elif s[0:3] in L:
            c = c+1
            s = s[3:]
        else:
            c = c+1
            s = s[1:]

print(c)