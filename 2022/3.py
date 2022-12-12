from string import ascii_lowercase, ascii_uppercase

def part1():
    with open('3.txt' , 'r') as f:
        scores = 0
        repeated_char = {}
        r = 0 
        for line in f.readlines():
            repeated_char[r] = set()
            for c in line[:len(line)//2]:
                if c in line[len(line)//2:]:
                    repeated_char[r].add(c) 
            r += 1

        uppercase_points = {i:char for char, i in enumerate(ascii_uppercase, 27)} 
        lowercase_points = {i:char for char, i in enumerate(ascii_lowercase, 1)}
        for c in repeated_char.values():
            c = str(*c)
            if c.isupper():
                scores += uppercase_points[c] 
            else:
                scores += lowercase_points[c] 
    
    print(scores)

def part2():
    with open('3.txt' , 'r') as f:
        scores = 0
        uppercase_points = {i:char for char, i in enumerate(ascii_uppercase, 27)} 
        lowercase_points = {i:char for char, i in enumerate(ascii_lowercase, 1)}
        repeated_char = {}
        r = 0 
        for line in f.readlines():
            repeated_char[r] = set(line.strip())
            r += 1
        for i in range(0, len(repeated_char), 3):
            for c in repeated_char[i]:
                if c in repeated_char[i+1] and c in repeated_char[i+2]:
                    if c.isupper():
                        scores += uppercase_points[c] 
                    else:
                        scores += lowercase_points[c] 

    print(scores)

part2()

# Below are the method I've learned from watching others code. 
"""
            common elements in multiple set

For common elements in multiple set we can use & operator:
    set1 & set2 & set3
     
    > set([1,2,2,3]) & set([2,4])
    {2}

"""
"""
            ord() function
We can use ord() function to find the value of each character:
    For example:
        ord('b') - ord('a') = 1 + 1
        ord('B') - ord('A') = 1 + 27
    note: the numbers being added is because of the problem wanted this order.
"""