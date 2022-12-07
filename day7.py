f = open('input.txt')
f.readline()
f.readline()
read_data = f.readlines()
f.close()

filesystem = ({},[])
curr_directory = [filesystem]
used_space = 0 
for data in read_data:
    if data[2:4] == "cd": 
        direct = data.split()[-1]
        if direct == "/": curr_directory = [filesystem]
        elif direct == "..": curr_directory.pop()
        else: curr_directory.append(curr_directory[-1][0][direct])
    elif data[2:4] == "ls": continue
    else:
        if data[:3] == "dir":
            if curr_directory[-1] == "/": 
                filesystem[0][data.split()[-1]] = ({},[]) 
            else: 
                curr_directory[-1][0][data.split()[-1]] = ({},[])
        else:
            value = int(data.split()[0])
            used_space += value
            if curr_directory[-1] == "/": 
                filesystem[1].append(value) 
            else: 
                curr_directory[-1][1].append(value)

dirs_size = []
def count_directory(directory,tot_sum):
    sum = 0
    count = (sum,tot_sum)
    for value in directory[1]:
        sum += value
    for d in directory[0]:
        count = count_directory(directory[0][d],tot_sum)
        sum += count[0]
        tot_sum = count[1]
    tot_sum += sum if sum <= 100000 else 0    
    dirs_size.append(sum)
    return (sum,tot_sum)

#Parte 1
print(count_directory(filesystem,0))

#Parte 2
unused_space = 70000000 - used_space
needed_space = 30000000 - unused_space
dirs_size.sort()
dirs_size = list(filter(lambda x: x >= needed_space, dirs_size))
print(dirs_size[0])






