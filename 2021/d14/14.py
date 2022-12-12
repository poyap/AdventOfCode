from collections import defaultdict, Counter
from os.path import dirname, join

# Reading from shell arguments
# path = sys.argv[1]

current_dir = dirname(__file__)
input_test_path = join(current_dir, 'it.txt')
input_path = join(current_dir, 'i.txt')

with open(input_path, 'r') as f:
    
    rules = {}
    for l in f:
        l = l.strip()
        if l.isalpha():
            template = l
        elif l:
            pairs, mid = l.split(' -> ')
            rules[pairs] = mid


def slow_approach():

    global template
    polymer = {}
    counter = 10
    steps_number = 0



    while counter:

        letter_count = Counter()

    
        length = len(template)
        for i in range(length-1):
    
            #  template[i][j]  == template_pair
            if template[i]+template[i+1] in rules:
                if steps_number+1 not in polymer:
                    polymer[steps_number+1] = ''
                if i == length-2:
                    polymer[steps_number+1] += template[i] + rules[template[i]+template[i+1]] + template[i+1]
            
                else:
                    polymer[steps_number+1] += template[i] + rules[template[i]+template[i+1]]
        letter_count[template[i]] += 1
        letter_count[template[i+1]] += 1
        letter_count[rules[template[i]+template[i+1]]] += 1

        template = polymer
        steps_number += 1
        counter -= 1

    print(polymer)
    print(letter_count)

# polymer[counter].u
# letters = polymer[10]
# letter_count = {}
# for l in letters:
#     letter_count[l] = letters.count(l)

# maximum = int(max(n for n in letter_count.values()))
# minimum = int(min(n for n in letter_count.values()))
# print(maximum- minimum, maximum, minimum)

# Expected 1749 - 161 = 1588


def faster_approach():
    
    """
    This approach uses less memory. because of it doesn't produce long string with 40 repeatition. 
    It will just count the characters.
    """
    pair_counts = Counter()
    for i in range(len(template)-1):
        pair_counts[template[i:i+2]] += 1
    for _ in range(40):
        new_count = Counter()
        char_count = Counter()
        for k , v in pair_counts.items():
            new_count[f'{k[0]}{rules[k]}'] += v
            new_count[f'{rules[k]}{k[1]}'] += v

            if _ == 39:  #This means when we are at the end of the loop.
                char_count[k[0]] += v
                char_count[rules[k]] += v

        pair_counts = new_count

    # Include the last char in template
    char_count[template[-1]] += 1


    """
    For sorting i approached in this two ways.
    """
    # maximum = int(max(n for n in char_count.values()))
    # minimum = int(min(n for n in char_count.values()))
    # print(maximum- minimum)
    print(sorted(char_count.values())[-1] - sorted(char_count.values())[0])
    """
    """

    print(new_count)
    print(char_count)

faster_approach()
