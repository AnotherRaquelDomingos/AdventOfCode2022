f = open('input.txt')
read_data = f.readlines()
f.close()

trees = []
for data in read_data:
    trees.append(list(map(int, data.split()[0])))
num_trees_cols = len(trees[0])     
num_trees_lines = len(trees)
num_trees = num_trees_cols * num_trees_lines 

#Parte 1
front_frontier = trees[0][1:-1]  
back_frontier = trees[-1][1:-1] 
right_frontier = list(map(lambda x: x[0], trees[1:-1]))  
left_frontier = list(map(lambda x: x[-1], trees[1:-1]))

sum = (num_trees_cols-2)*2 + (num_trees_lines-2)*2 + 4

curr_int_trees = []
num_int_trees = num_trees - 16
already_visible_trees = []
for tree in trees[1:-1]:
    curr_int_trees.append(tree[1:-1])

def look_in_frontiers(frontiers,curr_trees,ranges,sum,already_visible):
    for col in ranges[0]:
        for line in ranges[1]:
            visible = 0
            tree = curr_trees[line][col]
            if tree == "X": continue
            if  tree > frontiers[0][col]: 
                visible = 1
                frontiers[0][col] = tree
            if  tree > frontiers[1][line]:
                visible = 1 
                frontiers[1][line] = tree
            if visible and (line+1,col+1) not in already_visible:
                already_visible.append((line+1,col+1))
                sum += 1
    return (frontiers, already_visible, sum) 

ranges_1 = (range(num_trees_lines-2),range(num_trees_cols-2))    
ranges_2 = (list(reversed(ranges_1[0])),list(reversed(ranges_1[1]))) 

res = look_in_frontiers((front_frontier,right_frontier), curr_int_trees, ranges_1, sum, already_visible_trees)                
(front_frontier,right_frontier),already_visible_trees,sum = res
res = look_in_frontiers((back_frontier,left_frontier), curr_int_trees, ranges_2, sum, already_visible_trees)
(back_frontier,left_frontier),already_visible_trees,sum = res

print(sum)

#Parte 2
max_score = 0
highest_trees = set(already_visible_trees)

def get_tree_score(line,col,trees):
    height = trees[line][col]
    score_t,score_b,score_r,score_l = 0,0,0,0
    for top in reversed(range(0,line)):
        score_t += 1
        if trees[top][col] >= height: break 
    for left in reversed(range(0,col)):
        score_l += 1
        if trees[line][left] >= height: break 
    for bottom in range(line+1,num_trees_lines):
        score_b += 1
        if trees[bottom][col] >= height: break 
    for right in range(col+1,num_trees_cols):
        score_r += 1
        if trees[line][right] >= height: break
    return score_t*score_r*score_b*score_l   

for t in highest_trees:
    score_tree = get_tree_score(t[0],t[1],trees)    
    max_score = max(score_tree,max_score)  

print(max_score)           
        



