def solution(phone_number):
    answer = '*'*(len(phone_number)-4) + str(phone_number[-4:])
    return answer