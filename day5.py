import copy


f = open('input.txt')

stacks = []
stack_index = 0
to_move = False
moves = []

while f.readable:
    if not to_move:
        read_data = f.read(4)
        to_add = read_data[1]
        if to_add.isdigit():
            f.readline()
            f.readline()
            to_move = True
            continue
        if len(stacks) < stack_index+1: 
            stacks.append(list(to_add)) if to_add != " " else stacks.append([])
        else: 
            stacks[stack_index].append(to_add) if to_add != " " else  stacks
        stack_index = 0 if read_data[-1] == "\n" else stack_index + 1
    else:
        read_data = f.readline()
        if read_data == "": break
        read_data = read_data.split()
        moves.append((int(read_data[1]),int(read_data[3]),int(read_data[5])))        

f.close()

#Parte 1
stacks_1 = copy.deepcopy(stacks)
for st,fr,to in moves:
    for i in range(0,st):
        crate = stacks_1[fr-1].pop(0)
        stacks_1[to-1].insert(0,crate)  

message = list(map(lambda x: x[0],stacks_1))        
print(message)
   
#Parte 2
for st,fr,to in moves:
    crates = stacks[fr-1][0:st]
    stacks[fr-1] = stacks[fr-1][st:]
    stacks[to-1] = crates + stacks[to-1]
message = list(map(lambda x: x[0],stacks))        
print(message)   



