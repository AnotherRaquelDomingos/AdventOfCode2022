import re

f = open('input.txt')
read_data = f.readlines()
f.close()

pairs_areas = []
for data in read_data:
    data = re.split("\n|,|-",data)
    area1 = set(range(int(data[0]),int(data[1])+1))
    area2 = set(range(int(data[2]),int(data[3])+1))
    pairs_areas.append((area1,area2))

fully_contained_pairs = 0 #Parte1
overlapped_pairs = 0      #Parte2

for a1,a2 in pairs_areas:
    if (a1 <= a2 and len(a1-a2) == 0) or (a1 > a2 and len(a2-a1) == 0):  
        fully_contained_pairs += 1 
    if len(a1-a2) != len(a1): overlapped_pairs += 1    

print(fully_contained_pairs)        
print(overlapped_pairs)
