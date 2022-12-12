from collections import defaultdict
from os.path import dirname, join


current_dir = dirname(__file__)
input_test_path = join(current_dir, 'input_test.txt')
input_path = join(current_dir, 'input.txt')

with open(input_test_path, 'r') as f:
    edges = defaultdict(set)
    for line in f.readlines():
        src_path =line.split('-')[0]
        dst_path = line.strip('\n').split('-')[1]
        edges[src_path].add(dst_path)
        edges[dst_path].add(src_path)

    print(edges)
def part1():
    stck = [('start',)]
    all_path = set()
    while stck:
        
        poped_node = stck.pop()

        if poped_node[-1] == 'end':
            all_path.add(poped_node)
            continue

        for neighbour in edges[poped_node[-1]]:

            if neighbour not in poped_node or neighbour.isupper():
                stck.append((*poped_node, neighbour))

    print(len(all_path))
# part1()

def part2():
    """
    we can visit a single small cave twice
    """
    stck = [(('start',),False)]
    all_path = set()
    while stck:
        
        poped_node, double_visited = stck.pop()

        if poped_node[-1] == 'end':
            all_path.add(poped_node)
            continue
        
        for neighbour in edges[poped_node[-1]]:
            
            if neighbour == 'start':
                continue
            elif neighbour not in poped_node or neighbour.isupper():
                stck.append(((*poped_node, neighbour),double_visited))

            elif not double_visited and poped_node.count(neighbour) == 1:
                stck.append(((*poped_node, neighbour),True))
    return len(all_path)
part2()
