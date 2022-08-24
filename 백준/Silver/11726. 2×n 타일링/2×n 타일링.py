import sys
n = int(sys.stdin.readline())
result = [1,2]
for i in range(n-2):
    result.append(result[i]+result[i+1])

print(result[n-1]%10007)