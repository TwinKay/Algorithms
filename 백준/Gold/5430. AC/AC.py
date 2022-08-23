import sys

for _ in range(int(sys.stdin.readline())):

    a = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    num = sys.stdin.readline().rstrip()[1:-1].split(",")

    if a.count('D') <= n:
        left = 0
        right = 0
        judge = True
        for i in a:
            if i == 'R' and judge == True:
                judge = False
            elif i == 'R' and judge == False:
                judge = True
            else:
                if judge == True:
                    left += 1
                else:
                    right += 1

        if judge == True:
            if right != 0:
                del num[n-right:]
            if left != 0:
                del num[:left]

        else:
            num.reverse()
            if left != 0:
                del num[n-left:]
            if right != 0:
                del num[:right]

        print("[", end='')
        for j, i in enumerate(num):
            if j == len(num)-1:
                print(i,end='')

            else:
                print(i,end=',')
        print("]")

    else:
        print('error')