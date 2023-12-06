# brute force solution to day 5 puzzle 2

import re

with open('input.txt') as f:
    lines = f.readlines()
    seeds = []
    maps = {}
    loader_map = None
    locations = []
    start_seeds = []
    for line in lines:
        line = line.replace('\n', '')
        # Check for line contents and either a range coder or the seed list
        if re.match('^seeds: ', line):
            seeds = line.split(': ')[1]
            seeds = seeds.split(' ')
            # convert to int
            seeds = [int(seeds[i]) for i in range(0, len(seeds))]
            print(seeds)
        else:
            if re.match('.*map\:', line):
                prev_map = loader_map

                #print(f"Range coder: {line}")
                mfrom,mto = re.search('(.*)-to-(.*) map\:', line).groups()

                maps[mfrom] = {
                    'to': mto,
                    'from': prev_map,
                    'source':[],
                    'dest':[]
                }
                loader_map = mfrom
            # Is it a number?
            if re.match('[\d]', line) and loader_map != None:
                numbers = line.split(' ')
                numbers = [int(numbers[i]) for i in range(0, len(numbers))]
                #print(numbers)
                maps[loader_map]['source'].append({ 'start': numbers[1], 'end': numbers[1]+numbers[2] })
                maps[loader_map]['dest'].append({ 'start': numbers[0], 'end': numbers[0]+numbers[2] })
            # should cancel on blank line but I'm lazy
    print(maps)
    # loop though the seeds getting 2 numbers at a time
    for start, end in zip(*[iter(seeds)]*2):
        end=start+end
        for seed in range(start, end):
            start_seeds.append(seed)
            map_stage = 'seed'
            while map_stage != 'location':
                for srange in maps[map_stage]['source']:
                    if seed >= srange['start'] and seed < srange['end']:
                        seed = seed - srange['start'] + maps[map_stage]['dest'][maps[map_stage]['source'].index(srange)]['start']
                        break
                map_stage = maps[map_stage]['to']
            #print(f"Seed {seed} is in location")
            locations.append(seed)

    # find lowest location in the array
    lowest = min(locations)
    lowest_index = locations.index(lowest)
    print(f"Lowest seed: {start_seeds[lowest_index]}")
    print(f"Lowest: {lowest}")

