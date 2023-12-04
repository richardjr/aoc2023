import re

with open('input.txt') as f:
    grid = []
    sum= 0
    lines = f.readlines()

    for line in lines:
        line = line.replace('\n', '')
        grid_line = [char for char in line]
        grid.append(grid_line)
        print(line)
    grid_x = len(grid[0])
    grid_y = len(lines)
    print(f"Grid size: {grid_x}x{grid_y}")
    for x in range(0,grid_x):
        for y in range(0,grid_y):
            char = grid[y][x]
            if not re.match('[0-9.]', char):
                #  ray cast
                #print(f"found {char} {x},{y}")
                for dx in range(-1 , 2):
                    for dy in range(-1, 2):
                        x_mod= x+dx
                        y_mod= y+dy
                        #print(f"Checking {dx},{dy}")
                        check_char = grid[y_mod][x_mod]
                        if re.match('[0-9]', check_char) and not (dx == 0 and dy == 0):
                            start_x = x_mod
                            #print(f"Found ray {check_char} at {x_mod},{y_mod}")

                            # find the start of the number
                            for i in range(start_x, -1, -1):
                                if re.match('[0-9]', grid[y_mod][i]):
                                    start_x = i
                                else:
                                    break
                            #print(f"Start: {start_x}")
                            # find the end of the number
                            for i in range(start_x, grid_x):
                                if re.match('[0-9]', grid[y_mod][i]):
                                    end_x = i + 1
                                else:
                                    break
                            #print(f"End: {end_x}")
                            # make the string from start to end
                            string = ''.join(grid[y_mod][start_x:end_x])
                            # wipe the part from the grid
                            grid[y_mod][start_x:end_x] = ['.' for i in range(start_x, end_x)]

                            print(f"String: {string}")
                            sum += int(string)
    print(sum)


