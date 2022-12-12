def main():
    with open('test.txt' , 'r') as f:
        s, t , h = (0,0),(0,0),(0,0)
        tail_pos_count = 0
        for l in f.readlines():
            l = l.strip().split()
            direction, amount = l[0] , int(l[1])

            if direction == 'R':
                for _ in range(amount):
                    h = (h[0]+ 1, h[1])
                    if is_in_direction(t, h):
                        t = (h[0]-1, h[1])
                        tail_pos_count+= 1
                    else:
                        t = (h[0]-1, h[1]+1)
                        tail_pos_count+= 1

            elif direction == 'L':
                for _ in range(amount):
                    h = (h[0]- 1, h[1])
                    if is_in_direction(t, h):
                        t = (h[0]+ 1, h[1])
                        tail_pos_count+= 1
                    else:
                        t = (h[0]+ 1, h[1]-1)
                        tail_pos_count+= 1

            elif direction == 'U':
                for _ in range(amount):
                    h = (h[0], h[1] + 1)
                    if is_in_direction(t, h):
                        t = (h[0], h[1]-1)
                        tail_pos_count+= 1

                    else:
                        t = (h[0]+1, h[1]-1)
                        tail_pos_count+= 1

            else:
                for _ in range(amount):
                    h = (h[0],  h[1] - 1)
                    if is_in_direction(t, h):
                        t = (h[0], h[1]+1)
                        tail_pos_count+= 1
                    else:
                        t = (h[0]-1,  h[1]+1)
                        tail_pos_count+= 1  

    print(tail_pos_count)

def is_in_direction(pos1, pos2):
    if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
        return True
    else:
        return False

main()
