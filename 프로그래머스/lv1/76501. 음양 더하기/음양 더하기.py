def solution(absolutes, signs):
    answer = 0
    for i,j in enumerate(absolutes):
        if signs[i] == True:
            answer += j
        else:
            answer -= j
    return answer