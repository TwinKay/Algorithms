def solution(numbers):
    total = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                total.add(numbers[i]+numbers[j])
    total = list(total)
    total.sort()

    return total