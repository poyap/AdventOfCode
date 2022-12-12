def p1():
    with open('8.txt' , 'r') as f:
        # grid = f.read().strip()
        cords = {}
        count = 0
        

        for i, l in enumerate(f.readlines()):
            for j, n in enumerate(l.strip()):
                cords[j, i] = n
        grid_size = int(list(cords.keys())[-1][0])
        number_of_edges = grid_size * 4
        for i in cords:
            if 0 in i or grid_size in i:
                continue
            for j in adjacent_left(*i):
                if cords[j] >= cords[i]:
                    break
            else:
                count += 1
                continue
            for j in adjacent_right(*i, grid_size):
                if cords[j] >= cords[i]:
                    break
            else:
                count += 1
                continue
            for j in adjacent_down(*i, grid_size):
                if cords[j] >= cords[i]:
                    break
            else:
                count += 1
                continue
            for j in adjacent_up(*i):
                if cords[j] >= cords[i]:
                    break
            else:
                count += 1
    
    print(count , number_of_edges, count + number_of_edges)


def p2():
    cords = {}
    highest_score = 0
    with open('8.txt' , 'r') as f:
    
        for i, l in enumerate(f.readlines()):
            for j, n in enumerate(l.strip()):
                cords[j, i] = n
        grid_size = int(list(cords.keys())[-1][0])
        number_of_edges = grid_size * 4
        for i in cords:
            count_l = 0
            count_r = 0
            count_u = 0
            count_d = 0
            for j in adjacent_left(*i):
                if cords[j] >= cords[i]:
                    count_l += 1
                    break
                else:
                    count_l += 1
            for j in adjacent_right(*i, grid_size):
                if cords[j] >= cords[i]:
                    count_r += 1
                    break
                else:
                    count_r += 1
            for j in adjacent_down(*i, grid_size):
                if cords[j] >= cords[i]:
                    count_d += 1
                    break
                else:
                    count_d += 1

            for j in adjacent_up(*i):
                if cords[j] >= cords[i]:
                    count_u += 1
                    break
                else:
                    count_u += 1
            count_mul = count_l * count_r * count_d * count_u
            if count_mul > highest_score:
                highest_score = count_mul
    print(highest_score)


def adjacent_up(x,y, ):
    while y > 0 :
        y -= 1
        yield (x,y)

def adjacent_down(x,y, edge):
    while y < edge:
        y += 1
        yield (x,y)

def adjacent_right(x,y, edge):
    while x < edge:
        x += 1
        yield (x,y)

def adjacent_left(x,y, ):
    while x > 0:
        x -= 1
        yield (x,y)

p1()
p2()