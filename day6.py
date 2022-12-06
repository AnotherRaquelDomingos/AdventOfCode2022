f = open('input.txt')
read_data = f.read()
f.close()

processed = 0
possible_mark = ""

#Parte 1
for letter in read_data:
    if len(possible_mark) == 4: break
    else: 
       processed += 1 
       possible_mark = possible_mark.split(letter)[-1]
       possible_mark = possible_mark + letter 

print(processed)        

#Parte 2
processed = 0
for letter in read_data:
    if len(possible_mark) == 14: break
    else: 
       processed += 1 
       possible_mark = possible_mark.split(letter)[-1]
       possible_mark = possible_mark + letter 

print(processed)     
