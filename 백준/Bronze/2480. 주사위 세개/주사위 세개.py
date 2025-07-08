import sys

arr = list(map(int,sys.stdin.readline().split()))
arr.sort(reverse=True)
if arr[0]==arr[1] and arr[1]==arr[2] and arr[0]==arr[2]:
    print(10000+arr[0]*1000)
elif arr[0]==arr[1]:
    print(1000+arr[0]*100)
elif arr[1]==arr[2]:
    print(1000+arr[1]*100)
else:
    print(arr[0]*100)