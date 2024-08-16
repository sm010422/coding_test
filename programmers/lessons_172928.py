def solution(park, routes):
    height = len(park) 
    width = len(park[0])

    routes_num = len(routes)
    map_ = []
    routes_list = []
    start_h = 0 
    start_w = 0 
    x_location = []
    
    result = []
    
    
    for i in range(height):
        map_.append(list(park[i]))
    for j in range(routes_num):
        routes_list.append(list(routes[j]))
#find start_point
    for h in range(height):
        for w in range(width):
            if map_[h][w] == 'S':
                start_h = h
                start_w = w
    
    for h in range(height):
        for w in range(width):
            if map_[h][w] == 'X':
                x_location.append([h,w])

        
    
    def block_(start_height,start_width,x_loc,route_dir,how_much):
        compare_point = [start_height,start_width]
        return_value = True
        
        if route_dir == "E":
            for y in range(how_much):
                compare_point[1] = compare_point[1] + 1
                for x in range(len(x_loc)):
                    if compare_point == x_loc[x]:
                        return_value = False

        elif route_dir == "W":
            for y in range(how_much):
                compare_point[1] = compare_point[1] - 1
                for x in range(len(x_loc)):
                    if compare_point == x_loc[x]:
                        return_value = False

        elif route_dir == "S":
            for y in range(how_much):
                compare_point[0] = compare_point[0] + 1
                for x in range(len(x_loc)):
                    if compare_point == x_loc[x]:
                        return_value = False
                    
        elif route_dir == "N":
            for y in range(how_much):
                compare_point[0] = compare_point[0] - 1
                for x in range(len(x_loc)):
                    if compare_point == x_loc[x]:
                        return_value = False

        return return_value        
        

    
    def move_location(h_,w_,routes_list,x_loc):
        start_height = h_
        start_width = w_
        for n in range(len(routes_list)):
            route_dir = routes_list[n][0]
            if route_dir == 'E'   and start_width + int(routes_list[n][2]) < width and block_(start_height,start_width,x_loc,route_dir,int(routes_list[n][2])):
                start_width = start_width + int(routes_list[n][2])
                
            elif route_dir == 'W' and start_width - int(routes_list[n][2]) > -1 and block_(start_height,start_width,x_loc,route_dir,int(routes_list[n][2])):
                start_width = start_width - int(routes_list[n][2])
                
            elif route_dir == 'S' and start_height + int(routes_list[n][2]) < height and block_(start_height,start_width,x_loc,route_dir,int(routes_list[n][2])):
                start_height = start_height + int(routes_list[n][2])
                
            elif route_dir == 'N' and start_height - int(routes_list[n][2]) > -1 and block_(start_height,start_width,x_loc,route_dir,int(routes_list[n][2])):
                start_height = start_height - int(routes_list[n][2])
        
        result.append(start_height)
        result.append(start_width)
                
    
    move_location(start_h,start_w,routes_list,x_location)
    answer = result
    return answer
