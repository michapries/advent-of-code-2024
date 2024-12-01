import numpy as np
import pandas as pd
import datetime
import math
from collections import Counter


def get_day():
    return datetime.datetime.today().day


def get_input():
    with open(f'./day1/input.txt', 'r') as input:
        return input.readlines()
    

def get_testinput(task):
    if task not in [1, 2]:
        raise Exception('Not a valid task.')
    else:
        with open(f'./day1/testinput{task}.txt', 'r') as input:
            return input.readlines()


def main(is_part1):
    #input = [x.strip('\n').split() for x in get_testinput(1)]
    input = [x.strip('\n').split() for x in get_input()]

    # "Transpose" lists.
    left, right = [int(item[0]) for item in input], [int(item[1]) for item in input]

    if is_part1:
        # Elementwise subtraction between sorted left and right lists.
        diffs = [abs(l - r) for l, r in zip(sorted(left), sorted(right))]
        return sum(diffs)
    else:
        counter_right = Counter(right)
        return sum([l  * counter_right[l] for l in left])


print("Part 1:", main(True))
print("Part 2:", main(False))