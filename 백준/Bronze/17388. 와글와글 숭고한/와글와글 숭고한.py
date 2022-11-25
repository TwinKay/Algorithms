import sys

a,b,c = map(int, sys.stdin.readline().split())

if a+b+c >= 100:
    print('OK')
else:
    res = min(a,b,c)
    if res == a:
        print('Soongsil')
    elif res == b:
        print('Korea')
    else:
        print('Hanyang')