def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    cnt = sum(days[:a-1])+b-1
    cnt = cnt%7

    return week[cnt]