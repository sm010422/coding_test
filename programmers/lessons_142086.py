def solution(s):
    
    result = []
    
    
    for i in range(len(s)):
        w = 0
        y = 0
        for j in range(i):
            w += 1
            if s[i] == s[i - j - 1]:
                result.append(w)
                y = 1
                break
        if y == 0:
            result.append(-1)


                
    answer = result
    return answer
