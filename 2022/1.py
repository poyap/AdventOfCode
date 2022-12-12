with open('1.txt', 'r') as f:
    elves = {}
    counter = 0
    for line in f.readlines():
        line = line.strip()
        if line:
            line = int(line)
            if counter not in elves:
                elves[counter] = line
            else:
                elves[counter] += line
        else:
            counter += 1
    print(sum(sorted(elves.values())[-3:]))

s = [l.strip() for l in open('1.txt')]
s1 = '\n'.join(s).split('\n\n')
print(s1)