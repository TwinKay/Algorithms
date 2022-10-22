# 시험기간
import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '#':
        break
    else:
         cnt = 0
         for i in s:
             if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                 cnt += 1

         print(cnt)