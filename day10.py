f = open('input.txt')
read_data = f.readlines()
f.close()

instructions = []
for data in read_data:
    data = data.split()
    if data[0] == "noop": instructions.append((1,0))     
    else: instructions.append((2,int(data[1])))

cycles_marks = [20,60,100,140,180,220]
num_cyles = 1
x = 1
timeouts = 0
signal_strenghts = 0
curr_pos = 0
sprite_position = [0,3]

def print_get_strengths(cycles,strenghts,pos):
    if cycles in cycles_marks: strenghts += cycles*x
    if pos in range(sprite_position[0],sprite_position[1]): print("#",end="") 
    else: print(".", end="")     
    pos += 1
    if pos == 40:
        print()
        pos = 0    
    cycles += 1
    return (cycles,strenghts,pos)

for cyc,to_add in instructions:
    x += timeouts
    sprite_position = list(map(lambda y: y+timeouts, sprite_position))
    timeouts = to_add
    num_cyles,signal_strenghts,curr_pos = print_get_strengths(num_cyles,signal_strenghts,curr_pos)
    if cyc == 2:
        num_cyles,signal_strenghts,curr_pos = print_get_strengths(num_cyles,signal_strenghts,curr_pos)
x += timeouts       

print(signal_strenghts)
