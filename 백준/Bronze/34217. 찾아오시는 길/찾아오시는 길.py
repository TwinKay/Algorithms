import sys

A,B = map(int, sys.stdin.readline().split())
C,D = map(int, sys.stdin.readline().split())

if A+C < B+D:
    print("Hanyang Univ.")
elif A+C > B+D:
    print("Yongdap")
else:
    print("Either")