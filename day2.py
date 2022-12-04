
f = open('input.txt')
read_data = f.readlines()
f.close()

rounds = []
for line in read_data:
    line = tuple(line.split())
    rounds.append(line)

points_to_rock = {"A":3, "B":0, "C":6}
points_to_paper = {"A":6, "B":3, "C":0}
points_to_scissors = {"A":0, "B":6, "C":3}

to_lose = {"A":"Z", "B":"X", "C":"Y"}
to_draw = {"A":"X", "B":"Y", "C":"Z"}
to_win = {"A":"Y", "B":"Z", "C":"X"}

shapes_points = {"X":(1,points_to_rock,to_lose), 
                 "Y":(2,points_to_paper,to_draw), 
                 "Z":(3,points_to_scissors,to_win)
                }

#Parte 1
points = 0
for adv,me in rounds:
    my_points = shapes_points[me]
    points += (my_points[0] + my_points[1][adv])
print(points)    

#Parte 2
points = 0
for adv,dest in rounds:
    chosen_shape = shapes_points[dest][2][adv]
    my_points = shapes_points[chosen_shape]
    points += (my_points[0] + my_points[1][adv])

print(points)    


        
