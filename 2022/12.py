from string import ascii_lowercase

def get_neighbours(x,y):
    yield x+1, y
    yield x, y+1
    yield x-1, y
    yield x, y-1

def main():
    with open('12.txt' , 'r') as f:
        data = f.read().strip()

    alphabet = ascii_lowercase
    coords = {}
    row = 0
    col = 0
    for word in data:
        if word == 'S':
            start = (col, row)
        if word == '\n':
            row += 1
            col = 0
        else:
            coords[(col, row)] = word
            col += 1    
    stack = [start, ]
    counter = 0
    while stack:
        poped_node = stack.pop()
        poped_letter = coords[poped_node]
        if poped_letter == 'z':
            print(counter+1)
            return
        if poped_letter!='S':
            poped_node_index = alphabet.index(poped_letter)
        else:
            poped_node_index = 0
        for neighbour in get_neighbours(*poped_node):
            s = coords.get(neighbour, '')
            if s in ['E','S', '']:
                continue
            neighbour_index = alphabet.index(s)
            if neighbour_index <= poped_node_index+1 and neighbour not in stack:
                stack.append(poped_node)
                stack.append(neighbour)
                counter += 1
                break

main()