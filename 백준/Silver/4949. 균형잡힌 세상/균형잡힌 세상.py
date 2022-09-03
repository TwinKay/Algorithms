import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break
    else:
        count_small = 0
        count_big = 0
        pair = []

        for i in s:
            if i == '(':
                count_small += 1
                pair.append(True)

            elif i == '[':
                count_big += 1
                pair.append(False)

            elif i == ')':
                if count_small == 0:
                    count_small = -1  # 판단을 위한 0이 아닌 임의의 수
                    break
                else:
                    count_small -= 1
                    if pair.pop() == False:
                        count_small = -1  # 판단을 위한 0이 아닌 임의의 수
                        break

            elif i == ']':
                if count_big == 0:
                    count_small = -1  # 판단을 위한 0이 아닌 임의의 수
                    break
                else:
                    count_big -= 1
                    if pair.pop() == True:
                        count_small = -1  # 판단을 위한 0이 아닌 임의의 수
                        break

        if count_small == 0 and count_big == 0:
            print('yes')
        else:
            print('no')