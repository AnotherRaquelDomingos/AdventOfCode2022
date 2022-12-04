f = open('input.txt')
read_data = f.readlines()
f.close()

divided_rucksacks = []
group_rucksacks = []
new_group = []
for data in read_data:
    data = data.strip()
    new_group.append(set(data))
    if len(new_group) == 3:
        group_rucksacks.append(tuple(new_group))
        new_group = []
    half_data_len = len(data) // 2
    divided_rucksacks.append((set(data[:half_data_len]),set(data[half_data_len:])))

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Parte 1
tot_priorities = 0
for c1,c2 in divided_rucksacks:
    shared_item = list(c1 & c2)
    tot_priorities += priorities.index(shared_item[0])+1 

print(tot_priorities)    

#Parte 2
badges_total = 0
for e1,e2,e3 in group_rucksacks:
    badge = list(e1 & e2 & e3)
    badges_total += priorities.index(badge[0])+1

print(badges_total)
