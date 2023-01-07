def solution(numbers):
    l = list(range(10))
    for i in numbers:
        l.remove(i)
    return sum(l)