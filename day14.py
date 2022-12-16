import copy

paths_rock = []
sand_source = (500,0)
abyss_barrier = sand_source[1]  
infinite_floor = abyss_barrier

f = open('input.txt')
while f.readable():
    data = f.readline()
    if data == "": break
    data = data.split()
    coords = []
    for d in data:
        if d == "->": continue
        d = d.split(",")
        coords.append((int(d[0]),int(d[-1])))
    paths_rock.append(coords)    
f.close()

occupied = {}
for rocks in paths_rock:
    for i in range(len(rocks)-1):
        x1,y1 = rocks[i]
        x2,y2 = rocks[i+1]
        highest_y = max(y1,y2)
        abyss_barrier = highest_y if highest_y > abyss_barrier else abyss_barrier
        if x1 == x2:
            range_y = list(range(y1,y2+1)) if y1 < y2 else list(range(y2,y1+1))
            xx = [x1]*(abs(y1-y2)+1)
            for x in list(zip(xx,range_y)): occupied[x] = "#" 
        else:    
            range_x = list(range(x1,x2+1)) if x1 < x2 else list(range(x2,x1+1))
            yy = [y1]*(abs(x1-x2)+1)
            for x in list(zip(range_x,yy)): occupied[x] = "#" 
infinite_floor = abyss_barrier+2
occupied_2 = copy.deepcopy(occupied)


#Parte1
def falling_down_1(init_pos):
    curr_pos = init_pos
    if init_pos == False: return init_pos 
    while curr_pos not in occupied:
        curr_pos = (curr_pos[0],curr_pos[1]+1)
        if curr_pos[1]-1 >= abyss_barrier: return False 
    if (curr_pos[0]-1,curr_pos[1]) not in occupied:
        return falling_down_1((curr_pos[0]-1,curr_pos[1]))
    elif (curr_pos[0]+1,curr_pos[1]) not in occupied:      
        return falling_down_1((curr_pos[0]+1,curr_pos[1]))  
    return (curr_pos[0],curr_pos[1]-1) 

unit_sand = sand_source
num_units_sand = 0
while unit_sand != False:
    unit_sand = falling_down_1(sand_source)
    occupied[unit_sand] = "#"
    num_units_sand += 1

print(num_units_sand-1)

# Parte2
def falling_down_2(init_pos):
    curr_pos = init_pos
    while curr_pos[1] < infinite_floor and curr_pos not in occupied_2:
        curr_pos = (curr_pos[0],curr_pos[1]+1)
    if curr_pos[1] < infinite_floor and (curr_pos[0]-1,curr_pos[1]) not in occupied_2:
        return falling_down_2((curr_pos[0]-1,curr_pos[1]))
    elif curr_pos[1] < infinite_floor and (curr_pos[0]+1,curr_pos[1]) not in occupied_2:      
        return falling_down_2((curr_pos[0]+1,curr_pos[1]))  
    return (curr_pos[0],curr_pos[1]-1) 

unit_sand = sand_source
num_units_sand = 0
while sand_source not in occupied_2:
    unit_sand = falling_down_2(sand_source)
    occupied_2[unit_sand] = "#"
    num_units_sand += 1

print(num_units_sand)  