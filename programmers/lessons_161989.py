def solution(n, m, section):
    
    long = []
    count = 0
    
    for i in range(n):
        long.append([i+1,'O'])
    
    
    for i in section:
        long[i -1][1] = 'X'
    
    
    for i in range(len(long)):
        if long[i][1] == 'X':
            
            count = count + 1
            for j in range(m):
                if i+j >= len(long):
                    break
                else:
                    long[i+j][1] = 'O'
                    
        
    answer = count
    return answer
