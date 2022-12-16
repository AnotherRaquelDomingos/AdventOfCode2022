f = open('input.txt')
read_data = f.read()
f.close()

packets = []
stack = [packets]
prev_num = False
for data in read_data:
    if data.isdigit():
        if prev_num:
            stack[-1][-1] = stack[-1][-1] + data
        else:
            stack[-1].append(data)
            prev_num = True
    else:        
        if prev_num:
            prev_num = False
            stack[-1][-1] = int(stack[-1][-1])
        if data in  ["\n", ",", " ", ""]: continue
        elif data == "[": 
            stack[-1].append([])
            stack.append(stack[-1][-1])
        elif data == "]": stack.pop()
         

pairs_packets = []
for i in range(0,len(packets),2):
    pairs_packets.append((packets[i],packets[i+1]))

def in_right_order(list1,list2):
    len_1 = len(list1)
    len_2 = len(list2)
    for i in range(len_1):
        if i >= len_2: return False
        res = analise_elements(list1[i],list2[i])
        if res != None: return res
    return True if len_1 < len_2 else None

def analise_elements(elem1,elem2):
    type_1 = type(elem1) 
    type_2 = type(elem2)
    if type_1 == int and type_2 == int:
        if elem1 == elem2: return None
        return True if elem1 < elem2 else False
    if type_1 == list and type_2 == list: 
        return in_right_order(elem1,elem2)
    if type_1 == list and type_2 == int: 
        return in_right_order(elem1,[elem2])

    else: return in_right_order([elem1],elem2)

#Parte1
num_right_orders = 0
index = 1
for elem1,elem2 in pairs_packets:     
    if in_right_order(elem1,elem2): 
        num_right_orders += index
    index += 1

print(num_right_orders)    

#Parte2
index = 1
divider_1 = [[2]]
pre_divider_1 = 1
between_dividers_1_2 = 1 
divider_2 = [[6]]
for packet in packets:
    if in_right_order(packet,divider_1):
        pre_divider_1 += 1
    elif in_right_order(packet,divider_2):
        between_dividers_1_2 += 1

print(pre_divider_1*(between_dividers_1_2+pre_divider_1))






         
