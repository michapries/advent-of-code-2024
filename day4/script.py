# Use "regex" package instead of standard "re" package because it supports overlaps.
import regex as re

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    with open(f'./day4/{filename}', 'r') as input:
        return input.readlines()


def main(is_part1):
    # Replace newline character with P for regex parsing.
    text = [y.replace('\n', 'P') for y in get_input()]

    # Length of one line including P.
    l = len(text[0])

    text = ''.join(text)
    regexes = list()

    # Use regexes for every possible direction/permutation.
    if is_part1:
        regexes.append(re.findall('XMAS', text, overlapped=True))
        regexes.append(re.findall('SAMX', text, overlapped=True))
        regexes.append(re.findall(rf'X\w{{{l}}}M\w{{{l}}}A\w{{{l}}}S', text, overlapped=True))
        regexes.append(re.findall(rf'S\w{{{l}}}A\w{{{l}}}M\w{{{l}}}X', text, overlapped=True))
        regexes.append(re.findall(rf'X\w{{{l-1}}}M\w{{{l-1}}}A\w{{{l-1}}}S', text, overlapped=True))
        regexes.append(re.findall(rf'S\w{{{l-1}}}A\w{{{l-1}}}M\w{{{l-1}}}X', text, overlapped=True))
        regexes.append(re.findall(rf'X\w{{{l-2}}}M\w{{{l-2}}}A\w{{{l-2}}}S', text, overlapped=True))
        regexes.append(re.findall(rf'S\w{{{l-2}}}A\w{{{l-2}}}M\w{{{l-2}}}X', text, overlapped=True))
    else:
        regexes.append(re.findall(rf'M\w{{{1}}}S\w{{{l-2}}}A\w{{{l-2}}}M\w{{{1}}}S', text, overlapped=True))
        regexes.append(re.findall(rf'M\w{{{1}}}M\w{{{l-2}}}A\w{{{l-2}}}S\w{{{1}}}S', text, overlapped=True))
        regexes.append(re.findall(rf'S\w{{{1}}}S\w{{{l-2}}}A\w{{{l-2}}}M\w{{{1}}}M', text, overlapped=True))
        regexes.append(re.findall(rf'S\w{{{1}}}M\w{{{l-2}}}A\w{{{l-2}}}S\w{{{1}}}M', text, overlapped=True))

    return sum(len(regex) for regex in regexes)


print("Part 1:", main(True))
print("Part 2:", main(False))