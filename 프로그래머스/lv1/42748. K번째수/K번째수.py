def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        i,j,k = commands[a]
        new = array[i-1:j]
        new.sort()
        answer.append(new[k-1])

    return answer