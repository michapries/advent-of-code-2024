
import math
from collections import Counter

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    with open(f'./day5/{filename}', 'r') as input:
        return input.readlines()
            

def main(is_part1):
    inp = [x.strip('\n') for x in get_input()] 
    ordering, updates = inp[:inp.index('')], inp[inp.index('')+1:]
    ordering = [tuple(map(int, o.split('|'))) for o in ordering]
    updates = [list(map(int, update.split(','))) for update in updates]
    
    middle_sum = 0

    for update in updates:
        relevant_ordering = [k for k, v in ordering if k in update and v in update]
                
        # Sort numbers by how often they occur in the relevant orderings.
        # Does not include the number that is not in front of any other number (which would have a count of 0).
        sorted_counts = Counter(relevant_ordering).most_common()
        sorted_nums = [c[0] for c in sorted_counts]

        if is_part1 and update[:-1] == sorted_nums:
            middle_sum += update[math.floor(len(update)/2)]
        
        elif not(is_part1) and update[:-1] != sorted_nums:
            middle_sum += sorted_nums[int(len(sorted_nums)/2)]

    return middle_sum


print("Part 1:", main(True))
print("Part 2:", main(False))