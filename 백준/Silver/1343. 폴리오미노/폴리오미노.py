import sys

s = sys.stdin.readline().rstrip()
polio_before = list(s.split('.'))
polio = []
for i in polio_before:
    if i != '':
        polio.append(i)
    if len(i) % 2 == 1:
        print(-1)
        sys.exit(0)

polio_AB = []
for i in polio:
    if len(i)%4 == 0:
        polio_AB.append('AAAA'*(len(i)//4))
    else:
        polio_AB.append('AAAA'*(len(i)//4)+'BB')

result = []
jump = False
ind = 0
for i in s:
    if i == '.':
        result.append('.')
        jump = False
    elif jump == False:
        result.append(polio_AB[ind])
        ind += 1
        jump = True
    elif jump == True:
        pass

print(''.join(result))