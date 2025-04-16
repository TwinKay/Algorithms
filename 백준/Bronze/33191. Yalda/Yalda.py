import sys

budget = int(sys.stdin.readline())
watermelon_price = int(sys.stdin.readline())
pomegranates_price = int(sys.stdin.readline())
nuts_price = int(sys.stdin.readline())

if budget >= watermelon_price:
    print("Watermelon")
elif budget >= pomegranates_price:
    print("Pomegranates")
elif budget >= nuts_price:
    print("Nuts")
else:
    print("Nothing")
