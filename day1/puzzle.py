# load text file line by line
#
import re

with open('input.txt') as f:
    lines = f.readlines()
    clean_lines = [re.sub('[^0-9]', '', line) for line in lines]
    clean_lines = [line[0] + line[-1] if len(line) > 1 else line+line for line in clean_lines]
    result = sum([int(line) for line in clean_lines])
    print(result)

