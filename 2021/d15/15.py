from __future__ import annotations
from collections import defaultdict, Counter
from html import entities
from os.path import dirname, join
import heapq

# Reading from shell arguments
# path = sys.argv[1]

current_dir = dirname(__file__)
input_test_path = join(current_dir, '15t.txt')
input_path = join(current_dir, '15.txt')

with open(input_test_path, 'r') as f:
    
    risk_board = [l.strip() for l in f.readlines()]


"""
['1163751742',
 '1381373672',
 '2136511328',
 '3694931569', 
 '7463417111', 
 '1319128137', 
 '1359912421', 
 '3125421639', 
 '1293138521', 
 '2311944581',]
"""


def next_p(x,y):
    yield x+1, y
    yield x, y+1


def main(board:str) -> int:
    coords = {}
    for y, line in enumerate(board):
        for x, c in enumerate(line):
            coords[(x,y)] = int(c)

    last_x, last_y = max(coords)


    best_at: dict[tuple[int, int], int] = {}
    todo = [(0,(0,0))]
    while todo:
        cost, last_coord = heapq.heappop(todo)

        if last_coord in best_at and cost >= best_at[last_coord]:
            continue
        else:
            best_at[last_coord] = cost

        if last_coord == (last_x, last_y):
            return cost

        for cand in next_p(*last_coord):
            if cand in coords:  
                heapq.heappush(todo, (cost + coords[cand], cand))
    print(best_at)
    return best_at[(last_x, last_y)]

main(risk_board)




