from collections import namedtuple

square = {}
init_pos = 0
final_pos = 0
lines = 0
col = 0
num_col = 0
a_list = [] 

f = open('input.txt')
while f.readable():
    data = f.readline()
    if data == "": break
    data = data.split()[0]
    for d in data:
        if "S" == d: init_pos = (lines,col)
        if "E" == d: final_pos = (lines,col)  
        if "a" == d : a_list.append((lines,col))
        square[(lines,col)] = "SabcdefghijklmnopqrstuvwxyzE".index(d)
        col += 1
    num_col = col    
    col = 0
    lines += 1       
f.close()

pos_value = namedtuple("State_node","pos, value")

class State_node(pos_value):
    def __eq__(self,other):
        return isinstance(other,State_node) and self.pos == other.pos

def get_best_path(initial):
    if initial == final_pos: return 0
    frontier = [State_node(initial,0)]
    explored = set()
    while frontier:
        curr_pos,value = frontier.pop(0)
        explored.add(curr_pos)
        curr_line,curr_col = curr_pos
        if curr_pos == final_pos: return value
        possible_children = [(curr_line+1,curr_col),(curr_line-1,curr_col),(curr_line,curr_col+1),(curr_line,curr_col-1)]
        for pos in possible_children:
            line,column = pos
            child = State_node(pos,value+1) 
            if line >= 0 and line < lines and column >= 0 and column < num_col and square[curr_pos] >= (square[pos]-1) \
                                                                        and pos not in explored and child not in frontier:
                if pos == final_pos: return value +1                                                                        
                frontier.append(child)

res = get_best_path(init_pos)       
print(res)            

min = 0
for a in a_list:
    res = get_best_path(a)
    if res != None:
        min = res if min == 0 or res < min else min
print(min)        