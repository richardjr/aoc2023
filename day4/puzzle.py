import re

with open('input.txt') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
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
                if (card_sum == 0):
                    card_sum = 1
                else:
                    card_sum = card_sum * 2
        print(card_sum)
        sum += card_sum
    print(sum)
