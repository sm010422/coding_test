def solution(name, yearning, photo):

    dic = {}
    for index in range(len(name)):
        dic[index] = yearning[index]
    
    dic_yearing = {}
    for i in range(len(name)):
        dic_yearing[name[i]] = yearning[i] 
    
    sum_ = []
    positive = []
    sum_list = []
    
    def here_is2(name_, name,i):
        for j in range(len(name)):
            if name_ == name[j]:
                return dic_yearing[name_]
                
    def return_num(list):
        return list != None
    
    
    
    for i in range(len(photo)):
        for number in range(len(photo[i])):
            sum_list.append([])
            sum_list[i].append(here_is2(photo[i][number],name,i))
        positive = list(filter(return_num,sum_list[i]))
        sum_.append(sum(positive))

    print(sum_)
    
    answer = sum_
    return answer
