from collections import defaultdict
with open('11.txt' , 'r') as f:
    c = 0
    monkeies = {}
    for l in f.readlines():
        # print(l.strip().split())
        if l == '\n':
            c += 1
            monkeies[c] = {}
        if l.startswith('Monkey'):
            monkeies[c] = {}
        elif l.strip():
            l = l.strip()
            if l.startswith('Starting'):
                monkeies[c]['items'] = l.split(':')[1].split(',')
            elif l.startswith('Operation'):
                l = l.split(' ')
                monkeies[c]['Op'] = [l[-2], l[-1]]
            elif l.startswith('Test'):
                monkeies[c]['Test'] = [l.split(' ')[-1]]
            else:
                l = l.split(' ')
                if 'true' in l:
                    monkeies[c]['Test'] += l[-1]
                else:
                    monkeies[c]['Test'] += l[-1]
    round = 0
    monk_inspec_count = defaultdict(int)
    # find greates common multiple in all divisions value
    print(monkeies)
    lcm = 1
    DIV = [int(monkeies[i]['Test'][0]) for i in monkeies]
    # for i in monkeies:
    #     DIV.append(int(monkeies[i]['Test'][0]))

    for x in DIV:
        lcm *= (lcm*x)
    while round != 10000:
        for i in monkeies:
            len_items = len(monkeies[i]['items'])
            for _ in range(len_items):
                inspecting_el = int(monkeies[i]['items'][0])
                monkeies[i]['items'].pop(0)
                monk_inspec_count[i] += 1
                op_val = monkeies[i]['Op'][1]
                testing = monkeies[i]['Test']
                if monkeies[i]['Op'][0] == '*':
                    if op_val != 'old':
                        worry_level = int(op_val) * inspecting_el
                    else:
                        worry_level =  inspecting_el * inspecting_el
                
                if monkeies[i]['Op'][0] == '+':
                    if op_val != 'old':
                        worry_level = int(op_val) + inspecting_el
                    else:
                        worry_level =  inspecting_el + inspecting_el
                # if part==1
                # worry_level //= 3
                # else
                worry_level %= lcm
                if worry_level % int(testing[0]) == 0:
                    monkeies[int(testing[1])]['items'].append(worry_level)
                else:
                    monkeies[int(testing[-1])]['items'].append(worry_level)
            
        round += 1

# print(monkeies)
print(sorted(monk_inspec_count.items(), key=lambda x: x[1] )[-2:])          




"""
(in number theory) with respect to or using a modulus of a specified number. 
Two numbers are congruent modulo a given number if they give the same remainder when divided by that number.
19 and 64 are congruent modulo 5  19%5=4 and 64%5=4
"""