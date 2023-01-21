def solution(participant, completion):
    participant.sort()
    completion.sort()
    ans = ''
    for a,b in zip(participant,completion):
        if a != b:
            ans = a
            break
            
    if ans:
        return ans
    else:
        return participant[-1]
