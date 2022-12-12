from collections import defaultdict
from os.path import dirname, join
import re
import sys

# Reading from shell arguments
# path = sys.argv[1]

current_dir = dirname(__file__)
input_test_path = join(current_dir, 'input_test.txt')
input_path = join(current_dir, 'input.txt')

with open(input_path, 'r') as f:

    coords = set()
    folds = []
    while True:
        l = f.readline()
        
        if not l:
            break
        
        try:
            x, y = l.strip().split(',')
            x = int(x)
            y = int(y)
            coords.add((x,y))

        
        except:
            folds.append(re.findall(r'([xy]=\d+)', l))

print(folds)

for i in folds:
    
    if i:
        print(len(coords))
        fold_through, n = i[0].split('=')
        
        max_x = max(x for x, _ in coords)
        max_y = max(y for _, y in coords)

        # If we are folding through y axis
        if fold_through == 'y':
            coords = {
                (x, y if y < int(n) else max_y - y) for x,y in coords
                }
        # If we are folding through x axis
        elif fold_through == 'x':

            coords = {
                (x if x < int(n) else max_x - x, y) for x,y in coords
            }
            
                
         

   
max_x = max(x for x, _ in coords)
max_y = max(y for _, y in coords)
ans = ''
for y in range(0,max_y+1):
    for x in range(0,max_x+1):
        ans += ('#' if (x,y) in coords else ' ')
    print(ans)  
    ans = ''
print(len(coords))
print(coords)
        


            
# print(coords)

 



