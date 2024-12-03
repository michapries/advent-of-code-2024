import re

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    with open(f'./day3/{filename}', 'r') as input:
        return input.readlines()
            

def main(is_part1):
    input = ''.join(get_input())

    if not(is_part1):
        # Split at every do().
        do_split = re.split("do\(\)", input)

        # For every entry beginning with do, cut off everything after "don't".
        input = ''.join([re.split("don't\(\)", x)[0] for x in do_split])

    # List of matching mul strings.
    muls = re.findall('mul\(\d{1,3},\d{1,3}\)', input)
    
    # Extract integers.
    nums = [tuple(map(int, re.findall('\d+', mul))) for mul in muls]

    return sum([a * b for a, b in nums])


print("Part 1:", main(True))
print("Part 2:", main(False))