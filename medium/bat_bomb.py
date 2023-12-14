
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

# Binary search algorithm to find the position of Batman
# This function assumes that 'x', 'y', 'w', 'h', and 'bomb_dir' are available in the scope
# where this function is called.

def binary_search(x, y, w, h, bomb_dir):
    # Define the search space
    left, right = 0, w - 1
    top, bottom = 0, h - 1
    
    # Continue until the search space is valid
    while left <= right and top <= bottom:
        # Calculate the middle of the current search space
        mid_x = (left + right) // 2
        mid_y = (top + bottom) // 2
        
        # Narrow down the search space based on the bomb's direction
        if 'L' in bomb_dir:
            right = mid_x - 1
        if 'R' in bomb_dir:
            left = mid_x + 1
        if 'U' in bomb_dir:
            bottom = mid_y - 1
        if 'D' in bomb_dir:
            top = mid_y + 1
        
        # Update Batman's position to the middle of the new search space
        x = (left + right) // 2
        y = (top + bottom) // 2
    
    # Return the updated position
    return x, y

def search(bomb_dir):
    global left, right, up, down
    mid_x, mid_y = x, y
    if('L' in bomb_dir):
        mid_x = (x - left) // 2
        left = mid_x
        print(f"LEFT {mid_x}", file=sys.stderr, flush=True)
    elif('R' in bomb_dir):
        mid_x = x + (right - x) // 2
        right = mid_x
        print(f"RIGHT {mid_x}", file=sys.stderr, flush=True)
    if('U' in bomb_dir):
        mid_y = (y - up) // 2
        up = mid_y
        print(f"UP {mid_y}", file=sys.stderr, flush=True)
    elif('D' in bomb_dir):
        mid_y = y + (down - y) // 2
        down = mid_y
        print(f"DOWN {mid_y}", file=sys.stderr, flush=True)
    return mid_x, mid_y

    
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Update Batman's position using binary search
    x, y = search(x, y, w, h, bomb_dir)
    
    print(f"{x} {y}")