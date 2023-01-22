def solution(new_id):
    new_id = new_id.lower()
    
    num = ['1','2','3','4','5','6','7','8','9','0']
    from string import ascii_lowercase
    alpa = list(ascii_lowercase)
    s = []
    for i in new_id:
        if i in num or i in alpa or i == '-' or i == '_' or i == '.':
            s.append(i)
    
    s_3 = []
    check = False
    for i in s:
        if i == '.':
            if check == False:
                check = True
                s_3.append(i)
        else:
            s_3.append(i)
            check = False
    
    if s_3[0] == '.':
        if len(s_3) == 1:
            s_3 = ['a']
        else:
            s_3 = s_3[1:]
    if s_3[-1] == '.':
        if len(s_3) == 1:
            s_3 = ['a']
        else:
            s_3.pop()
    
    if len(s_3) >= 16:
        s_3 = s_3[:15]
        
    if s_3[-1] == '.':
        s_3.pop()
    
    if len(s_3) == 1:
        s_3.append(s_3[-1])
        s_3.append(s_3[-1])
    elif len(s_3) == 2:
        s_3.append(s_3[-1])
        
    return ''.join(s_3)