
with open('6.txt' , 'r') as f:
    file_ = f.read().strip()
    ch_counter = 0
    string = ''
    index = 0
    for c in file_:
        string += c
        if len(string) >= 14:
            fourth = string[index:index+14]
            if len(set(fourth)) == 14:
                ch_counter += 1
                break
            else:
                index += 1
        ch_counter += 1

print(ch_counter)