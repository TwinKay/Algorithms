s = input().strip()
parts = s.split('-')
answer = ''.join(p[0] for p in parts)
print(answer)