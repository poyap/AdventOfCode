with open('10.txt' , 'r') as f:

    inst_cycle = {'noop':1, 'addx': 2}
    current_cycle = 0
    x = 1
    crt = [[' ' for _ in range(40)] for _ in range(6)]
    row = 0
    column = 0
    strike_pos = (0,1,2)
    list_of_cycle = [20, 60, 100, 140, 180, 220]
    signal_strenght = []
    for line in f.readlines():
        strike_pos = (x-1, x, x+1)
        line = line.strip().split()

        for _ in range(inst_cycle[line[0]]):  
    
            if column in strike_pos:
                crt[row][column] = '#'
            if column < 39:
                column+=1 
            else:
                column = 0
                row += 1  
            current_cycle += 1      
            if current_cycle in list_of_cycle:
                signal_strenght.append(x*current_cycle)
        if len(line) == 2:
            x += int(line[1])

print(sum(signal_strenght))
for r in range(6):
    print(''.join(crt[r]))



"""
(Jonathin paulson's solution) Another way to handle strike position is to check if:
    abs(x-(current_cycle%40)) <= 1
    40 is for the length of the rows;
    and acording to problem we just need to handle position of strike in rows(not column).

Also another way to handle the position to draw '#' or '.' is:

G = [['?' for _ in range(40)] for _ in range(6)]
t is the timing of the cycle. increment by one. it is equalent to current_cycle of mine solution.
p1 is the answer of part 1.
    def handle_tick(t, x):
        global p1
        global G
        t1 = t-1
        G[t1//40][t1%40] = ('#' if abs(x-(t1%40))<=1 else ' ')
        if t in [20, 60, 100, 140, 180, 220]:
            p1 += x*
"""