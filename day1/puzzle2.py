# load text file line by line
#

with open('input.txt') as f:
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    lines = f.readlines()
    sum = 0
    for line in lines:
        clean_line = ""
        for j in range(0, len(line)):
            if line[j].isdigit():
                clean_line += line[j]
            elif line[j].isalpha():
                for i in range(0, len(words)):
                    if line[j:j+len(words[i])] == words[i]:
                        clean_line += str(i+1)
                        break
        if len(clean_line) > 1:
            clean_int = int(clean_line[0] + clean_line[-1])
        else:
            clean_int = int(clean_line+clean_line)
        print(clean_line)
        print(clean_int)
        sum += clean_int
    print(sum)