from utils import *
 
f = open('input.txt')
read_data = f.readlines()
f.close()

calories_list = []
new_list = []
for data in read_data:
    if data == "\n": 
        calories_list.append(new_list)
        new_list = []
    else:
        data = data.strip()
        new_list.append(int(data)) 
calories_list.append(new_list)        

max_calories_queue = PriorityQueue(f=sum)
for x in calories_list:
    max_calories_queue.append(x)


max_calories_list = max_calories_queue.A 
max_calories_list = list(map(lambda x: x[0], max_calories_list[-3::1]))    

#Parte1
max_calories = max_calories_list[-1]
print(max_calories)

#Parte2
max_calories_three = sum(max_calories_list)
print(max_calories_three)
    