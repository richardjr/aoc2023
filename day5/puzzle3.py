
with open('input.txt') as f:
    lines = f.read().split('\n\n')
    lines = [line.split('\n') for line in lines]
    seeds = [int(seed) for seed in lines[0][0].split(':')[1].split()]
    seeds = [[seeds[a], seeds[a] + seeds[a+1]-1] for a in range(0, len(seeds), 2)]
    groups = lines[1:]
    for group in groups:
        i = 0
        # we are appending idiot don't use a for loop range ffs
        while i < len(seeds):
            in_range = False
            start, end = seeds[i]
            for line in group[1:]:
                dest, source, amount = [int(val) for val in line.split()]
                if in_range is False:
                    # Start falls in range of map
                    if start >= source and start < (source + amount):
                        in_range = True
                        seeds[i][0] = dest + (start - source)
                        # Is end also in that range?
                        if end < source + amount:
                            seeds[i][1] = dest + (end - source)
                            print(f"Moving seed end {end} to {dest + (end - source)}")
                        # No, so we need to split the seed
                        else:
                            seeds[i][1] = dest + amount
                            print(f"Moving seed end {end} to {dest + amount}")
                            seeds.append([source + amount, end])
                            print(f"Adding seed {source + amount} to {end}")
                    # Ok what about the end?
                    elif end >= source and end < (source + amount):
                        in_range = True
                        #mode the end to the....end ;)
                        seeds[i][1] = dest + (end - source)
                        # Start in range? split
                        if start > source:
                            seeds[i][0] = dest + (start - source)
                            print(f"Moving seed start {start} to {dest + (start - source)}")
                        else:
                            # start is not in range so we need to split the seed
                            seeds[i][0] = dest
                            print(f"Moving seed start {start} to {dest}")
                            # Why did we overlap without -1, I think my brain is dead
                            seeds.append([start, source-1])
                            print(f"Adding seed {start} to {source-1}")
            i += 1
    print(seeds)
    lowest = None
    for seed in seeds:
        new_min=min([seed[0], seed[1]])
        if lowest is None or new_min < lowest:
              lowest = new_min
    print(lowest)

