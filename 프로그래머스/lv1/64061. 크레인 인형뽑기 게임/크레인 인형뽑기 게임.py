def solution(board, moves):
    n = len(board)
    stack = []
    for _ in range(n):
        stack.append([])
    
    for i in board[::-1]:
        for a,j in enumerate(i):
            if j != 0:
                stack[a].append(j)
    
    cnt = 0
    basket = [-1]
    for i in moves:
        i -= 1
        if stack[i]:
            temp = stack[i].pop()
        
            if basket[-1] == temp:
                if basket:
                    basket.pop()
                    cnt += 2
            else:
                basket.append(temp)

    return cnt