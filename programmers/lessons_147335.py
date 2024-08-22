def solution(t, p):
    
    result = 0;
    
        
    for i in range(len(t) - len(p) + 1):
        a = 0
        for j in range(len(p)):
            a = a + int(t[i+j])*pow(10,len(p)-j-1)
        if a <= int(p):
            result += 1;
        
        
    
    print('result:',result)
    
    answer = result
    return answer
