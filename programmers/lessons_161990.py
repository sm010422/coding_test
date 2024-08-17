def solution(wallpaper):
    
    height = len(wallpaper)
    width = len(wallpaper[0])
    
    list_ = []
    map_ = []

    result = [0,0,0,0]


    for i in range(height):
        map_.append(list(wallpaper[i]))
        
    for x in range(height):
        for y in range(width):
            if map_[x][y] == '#':
                list_.append([x,y])
                

    result[0] = list_[0][0]
    result[2] = list_[len(list_)-1][0] + 1
    
    smallest_x = list_[0][1]
    largest_x = list_[0][1]
    
    
    for a in range(len(list_)):
        if smallest_x > list_[a][1]:
            smallest_x = list_[a][1]
    result[1] = smallest_x
    
    for b in range(len(list_)):
        if largest_x < list_[b][1]:
            largest_x = list_[b][1]
    result[3] = largest_x + 1
            
    
    print('height:',height)
    print('width:', width)
    print('list:',list_)
    print('result:',result)
    
    answer = result
    return answer
