import re

with open('input.txt') as f:
    lines = f.readlines()
    seeds = []
    maps = {}
    loader_map = None
    locations = []
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
                #print(f"Range coder: {line}")
                mfrom,mto = re.search('(.*)-to-(.*) map\:', line).groups()

                maps[mfrom] = {
                    'to': mto,
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
    for seed in seeds:
        map_stage = 'seed'
        #print(f"Running: {seed}")
        while map_stage != 'location':
            for range in maps[map_stage]['source']:
                if seed >= range['start'] and seed < range['end']:
                    seed = seed - range['start'] + maps[map_stage]['dest'][maps[map_stage]['source'].index(range)]['start']
                    break
            map_stage = maps[map_stage]['to']
            #print(f"maps to: {seed} in {map_stage}")
        print(f"Seed {seed} is in location")
        locations.append(seed)

    # find lowest location in the array
    lowest = min(locations)
    print(f"Lowest: {lowest}")

