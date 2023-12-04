# load file line by line
#
import re

with open('input.csv') as f:
    cubes = {'red': 12, 'blue': 14, 'green': 13}
    lines = f.readlines()
    sum = 0
    for line in lines:
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
                    fail = True
                    break
        if fail == False:
            print('Cubes pass for game: ' + game_id)
            sum += int(game_id)
    print(sum)
