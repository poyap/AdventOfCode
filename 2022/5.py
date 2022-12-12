
with open('5.txt' , 'r') as f:
    file_ = f.read()
    crates, proc = file_.split('\n\n')
    MOVES = []
    for p in proc.split('\n'):
        moves = []
        for c in p.split():
            if c.isnumeric():
                moves.append(c)

        MOVES.append(moves)


    board = []
    for line in crates.split('\n'):
        if line == '':
            break
        sz = (len(line)+1)//4
        while len(board) < sz:
            board.append([])
        for i in range(len(board)):
            ch = line[1+4*i]        
            if ch != ' ' and ch.isupper():
                board[i].append(ch)

    for i in MOVES:
        quantity = int(i[0])
        from_ = int(i[1])-1
        to = int(i[2])-1

        board[to] = board[from_][:quantity] + board[to]
        board[from_] = board[from_][quantity:]
        # for _ in range(quantity):
        #     # print(board)
        #     board[to].insert(0, board[from_][0]) 

    print(''.join(i[0] for i in board))
    ''.join([i[0] for i in board])