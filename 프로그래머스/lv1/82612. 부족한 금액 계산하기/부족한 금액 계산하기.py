def solution(price, money, count):
    total = 0
    for i in range(count+1):
        total += i*price
    if total >= money:
        ans = total-money
    else:
        ans = 0
    return ans