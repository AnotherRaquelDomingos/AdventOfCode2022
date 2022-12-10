f = open('input.txt')
read_data = f.readlines()
f.close()

moves = []
for data in read_data:
    data = data.split()
    moves.append((data[0],int(data[1])))

directions = {"R": (lambda x: (x[0],x[1]+1)), "L": (lambda x: (x[0],x[1]-1)),
              "U": (lambda x: (x[0]+1,x[1])), "D": (lambda x: (x[0]-1,x[1]))} 

positions_tail = {(0,0)}
head_pos = (0,0)
tail_pos = (0,0)

#Parte 1
def verify_tail(tail,head):
    diff_0 = head[0] - tail[0]
    diff_1 = head[1] - tail[1]
    if tail[0] - head[0] > 1: return (tail[0]-1,tail[1]+diff_1)
    if tail[1] - head[1] > 1: return (tail[0]+diff_0,tail[1]-1)
    if head[0] - tail[0] > 1: return (tail[0]+1,tail[1]+diff_1)
    if head[1] - tail[1] > 1: return (tail[0]+diff_0,tail[1]+1)
    return tail

for dir,n in moves:
    for i in range(0,n):
        head_pos = directions[dir](head_pos)
        tail_pos = verify_tail(tail_pos,head_pos) 
        positions_tail.add(tail_pos)

print(len(positions_tail))

#Parte 2
knots_num = 9
knots_positions = list((0,0) for x in range(0,knots_num))
head_pos = (0,0)
positions_tail = {(0,0)}

def verify_tails_knots(tail,head):
    if abs(tail[1] - head[1]) > 1 and abs(tail[0] - head[0]) > 1:
        if tail[0] - head[0] > 1: 
            return (tail[0]-1,tail[1]-1) if tail[1] - head[1] > 1 else (tail[0]-1,tail[1]+1)
        if head[0] - tail[0] > 1: 
            return (tail[0]+1,tail[1]-1) if tail[1] - head[1] > 1 else (tail[0]+1,tail[1]+1) 
            
    return verify_tail(tail,head)

def verify_knots(knots,knots_n,head):
    knots[0] = verify_tails_knots(knots[0],head)
    for i in range(1,knots_n):
        knots[i] = verify_tails_knots(knots[i],knots[i-1])
    return knots    

for dir,n in moves:
    for i in range(0,n):
        head_pos = directions[dir](head_pos)
        knots_positions = verify_knots(knots_positions,knots_num,head_pos) 
        positions_tail.add(knots_positions[-1])

print(len(positions_tail))        