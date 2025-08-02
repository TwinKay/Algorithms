'''
아이디어:
원자량 자체를 스택으로 이용하는 방법
( 도 스택에 넣고, )가 나오면 (가 나올 때까지 pop하며 더하고 해당 더한 결과를 append
숫자가 나오면 이전값 pop해서 곱하고 다시 넣기
'''

import sys

S = sys.stdin.readline().rstrip()

stack = []
i = 0
while i < len(S):
    c = S[i]

    if c == 'H':
        stack.append(1)
        i += 1
    elif c == 'C':
        stack.append(12)
        i += 1
    elif c == 'O':
        stack.append(16)
        i += 1
    elif c == '(':
        stack.append('(')
        i += 1
    elif c == ')':
        temp = 0
        while stack[-1] != '(':
            temp += stack.pop()
        stack.pop()
        stack.append(temp)
        i += 1
    elif c.isdigit():  # python에서 숫자 확인법
        num = int(c)
        temp = stack.pop()
        stack.append(temp * num)
        i += 1

print(sum(stack))
