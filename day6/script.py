import numpy as np
import pandas as pd
import datetime
import math

def get_day():
    return datetime.datetime.today().day


def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    with open(f'./day6/{filename}', 'r') as input:
        return input.readlines()
            

def part1():
    mappa = np.array([list(line.strip('\n')) for line in get_input()])

    start_index = np.where(mappa == '^')
    
    i,j = start_index[0][0], start_index[1][0]
    #dir = 'up'

    # Directions in order of how we will cycle through them.
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]

    direction_changes = 0
    while 0 <= i < mappa.shape[0] and 0 <= j < mappa.shape[1]:
        #print(i, j)
        
        new_dirs = dirs[direction_changes % 4]
        mappa[i][j] = 'X'
        if i+new_dirs[0] == mappa.shape[0] or j+new_dirs[1] == mappa.shape[1]:
            break
        elif mappa[i+new_dirs[0]][j+new_dirs[1]] == '#':
            direction_changes += 1
            new_dirs = dirs[direction_changes % 4]
            
        
        i += new_dirs[0]
        j += new_dirs[1]

    print(mappa)
    return np.count_nonzero(mappa == 'X') 


def part2():
    mappa = np.array([list(line.strip('\n').replace('.', [])) for line in get_input(1)])

    start_index = np.where(mappa == '^')
    print(mappa)
    i,j = start_index[0][0], start_index[1][0]
    #dir = 'up'

    # Directions in order of how we will cycle through them.
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]

    direction_changes = 0
    while 0 <= i < mappa.shape[0] and 0 <= j < mappa.shape[1]:
        #print(i, j)
        
        new_dirs = dirs[direction_changes % 4]
        mappa[i][j] = 'X'
        if i+new_dirs[0] == mappa.shape[0] or j+new_dirs[1] == mappa.shape[1]:
            break
        elif mappa[i+new_dirs[0]][j+new_dirs[1]] == '#':
            direction_changes += 1
            new_dirs = dirs[direction_changes % 4]
            
        
        i += new_dirs[0]
        j += new_dirs[1]

    print(mappa)
    return np.count_nonzero(mappa == 'X') 


def main(is_part1):
    if is_part1:
        return part1()
    else:
        return part2()


#print("Part 1:", main(True))
print("Part 2:", main(False))