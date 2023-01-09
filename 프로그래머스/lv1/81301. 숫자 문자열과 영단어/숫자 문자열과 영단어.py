def solution(s):
    dic = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight','9': 'nine'}
    
    res = ''
    trash = ''
    for i in range(len(s)):
        if s[i] in dic.keys():
            res += s[i]
        else:
            trash += s[i]
            if trash in dic.values():
                for k,v in dic.items():
                    if v == trash:
                        res += k
                trash = ''

    return int(res)


