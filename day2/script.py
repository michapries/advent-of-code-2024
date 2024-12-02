import numpy as np
import pandas as pd
import datetime
import math

def get_day():
    return datetime.datetime.today().day


def get_input():
    with open(f'./day2/input.txt', 'r') as input:
        return input.readlines()
    

def get_testinput(task):
    if task not in [1, 2]:
        raise Exception('Not a valid task.')
    else:
        with open(f'./day2/testinput{task}.txt', 'r') as input:
            return input.readlines()


# Returns True if report is safe, False otherwise.
def is_report_safe(report, diffs):
    sorted_report = sorted(report)
    return (report == sorted_report or report == list(reversed(sorted_report))) and all(abs(item) in [1,2,3] for item in diffs)


def main(is_part1):
    #input = [list(map(int, x.strip('\n').split())) for x in get_testinput(1)]
    input = [list(map(int, x.strip('\n').split())) for x in get_input()]

    safe_reports = 0

    for report in input:

        # Calculate diff vector for each report.
        diffs = [report[i] - report[i-1] for i in range(1, len(report))]
        
        if is_report_safe(report, diffs):
            safe_reports += 1
        elif not(is_part1):
            # "Brute force" part 2 by actually removing each element and checking if it fits the criteria.
            for i in range(len(report)):
                truncated_report = report[:i] + report[i+1:]
                truncated_diffs = [truncated_report[i] - truncated_report[i-1] for i in range(1, len(truncated_report))]
                
                if is_report_safe(truncated_report, truncated_diffs):
                   safe_reports += 1
                   break

    return safe_reports


print("Part 1:", main(True))
print("Part 2:", main(False))