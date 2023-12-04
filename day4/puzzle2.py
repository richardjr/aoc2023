import re

with open('input.txt') as f:
    line_copies = []
    lines = f.readlines()
    # init the line_copies to 1
    for line in lines:
        line_copies.append(1)
    sum = 0
    for index,line in enumerate(lines):
        line = line.replace('\n', '')
        # lost the Card x: part
        line = line.split(': ')[1]
        win, have = line.split('|')
        win = [int(win[i:i + 3]) for i in range(0, len(win), 3)]
        have = [int(have[i:i + 3]) for i in range(0, len(have), 3)]
        # check every win to see if it exists in have
        card_sum = 0
        for i in win:
            if i in have:
                card_sum += 1
        print(card_sum)
        for copies in range(0,line_copies[index]):
            for j in range(index+1, index+1+card_sum):
                line_copies[j] += 1
    print(line_copies)
    for i in line_copies:
        sum += i
    print(sum)
