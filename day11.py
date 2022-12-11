import copy

operations = {"*": (lambda x, y: x*y), "+": (lambda x, y: x+y)}
monkeys = {}
index = -1
mmc = 1

f = open('input.txt')
while f.readable():
    #Monkey number
    if (f.readline() == ""): break
    index += 1
    monkeys[index] = []
    #Starting items: num1 num2 ...
    monkeys[index].append(list(map(lambda x: int(x.split(",")[0]), f.readline().split()[2:])))
    #Operation: new = ...
    data = f.readline().split()
    monkeys[index].append(((operations[data[-2]],int(data[-1])) if data[-1].isdigit() else (operations[data[-2]],None)))
    #Test: divisible by number
    num = int(f.readline().split()[-1])
    monkeys[index].append(num)
    mmc *= num
    #If true: throw to monkey num / If false: throw to monkey num
    for i in range(0,2):
        monkeys[index].append(int(f.readline().split()[-1]))
    f.readline()    
f.close()

num_monkeys = index + 1
monkeys_inspections = [0] * num_monkeys

def monkeys_round(monkeys,n_monkeys,monkeys_insp):
    for m in range(0,n_monkeys):
        items,op,test,t,f = monkeys[m]
        for item in items:
            op_num = op[1] if op[1] != None else item 
            #Parte 1 
            # item = (op[0](op_num,item)) % mmc 
            #Parte 2
            item = (op[0](op_num,item)) % mmc 
            monkeys[t][0].append(item) if item % test == 0 else monkeys[f][0].append(item)
            monkeys_insp[m] += 1
        monkeys[m][0] = []     

for j in range(0,10000):
    monkeys_round(monkeys,num_monkeys,monkeys_inspections)

monkeys_inspections.sort()
print(monkeys_inspections[-2]*monkeys_inspections[-1])