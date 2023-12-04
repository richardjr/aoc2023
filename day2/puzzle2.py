# load file line by line
#
import re

with open('input.csv') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        fail = False
        bits = line.split(';')
        game_id = re.sub('[A-Za-z]', '', bits[0].split(':')[0])
        bits[0] = re.sub('.*:', '', bits[0])
        for bit in bits:
            bit = bit.replace(' ', '')
            smaller_bits = bit.split(',')
            for j in smaller_bits:
                vals = re.search('([0-9]{1,2})(.*)', j)
                if int(vals.group(1)) > cubes[vals.group(2)]:
                    cubes[vals.group(2)] = int(vals.group(1))
        power=cubes['red']*cubes['green']*cubes['blue']
        sum += power
        print(power)

    print(sum)
