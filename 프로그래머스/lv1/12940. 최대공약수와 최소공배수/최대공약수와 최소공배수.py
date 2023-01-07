def solution(n, m):
    n_l = []
    m_l = []
    for i in range(1,(int(n**(1/2)))+1):
        if (n/i)%1 == 0:
            n_l.append(i)
            n_l.append(int(n/i))

    for i in range(1,(int(m**(1/2)))+1):
        if (m/i)%1 == 0:
            m_l.append(i)
            m_l.append(int(m/i))
    
    n_l.sort()
    m_l.sort()
    for i in n_l[::-1]:
        if i in m_l:
            a = i
            break

    for i in range(max(n,m),1000001):
        if i%n == 0 and i%m == 0:
            b = i
            break

    answer = [a,b]
    return answer