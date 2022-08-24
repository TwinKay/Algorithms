import sys
n = int(sys.stdin.readline())
result = [1,3]
for i in range(n-2):
    result.append(result[i]*2+result[i+1])

print(result[n-1]%10007)