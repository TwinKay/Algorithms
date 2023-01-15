import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

if a<2:
    print('Before')
elif a>2:
    print('After')
else:
    if b<18:
        print('Before')
    elif b>18:
        print('After')
    else:
        print('Special')