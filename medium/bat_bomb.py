
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ----------> LINK = https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1-codesize
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]

mov = {"U": (0, -1), "UR": (1, -1), "R": (1, 0), "DR": (1, 1), "D": (0, 1), "DL": (-1, 1), "L": (-1, 0), "UL": (-1, -1)}
pos = []
def countDir(lst):
    c = 1
    ln = len(lst)
    if(ln >= 2):
        i = ln - 2

        while(lst[ln - 1] == lst[i] and i > 0):
            c += 1
            i -= 1
    return c
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    pos.append(bomb_dir)
    # Write an action using print
    print(f"{bomb_dir} - {mov[bomb_dir]}", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    dx, dy = mov[bomb_dir]
    x += dx * countDir(pos)
    y += dy * countDir(pos)
    if(x >= w):
        x = w - 1
    if(y >= h):
        y = h - 1
    
    print(f"{x} {y}")