with open('4.txt' , 'r') as f:
    fully_overlap = 0
    partially_overlap = 0
    for line in f.readlines():
        line = line.strip()
        p1, p2 = line.split(',')
        p1 = p1.split('-')
        p2 = p2.split('-')
        p1 = list(range(int(p1[0]),int(p1[-1])+1))
        p2 = list(range(int(p2[0]),int(p2[-1])+1))
        # part1
        if all(el in p2 for el in p1) or all(el in p1 for el in p2):
            fully_overlap+=1 
        # part2
        if any(el in p2 for el in p1):
            partially_overlap+=1 

print('Part1: ', fully_overlap)
print('Part2: ', partially_overlap)



# Below are the method I've learned from watching others code. 
"""
* Assigning values of a list to variables below:
    s1,e1, s2, e2 = [int(x) for x in [2,3,4,5]]
    result: s1=2, e1=3 , ...
* Another way to calculate overpaling is, we can just use start, end of the period of each two period.
    rather than making a whole list of the range and check if any element of first one in the second as I've 
    done that above. 
"""
