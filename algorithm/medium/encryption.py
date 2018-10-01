# An English text needs to be encrypted using the following encryption scheme.
# First, the spaces are removed from the text. Let L be the length of this text.
# Then, characters are written into a grid, whose rows and columns have the following constraints:
import math


def encryption(s):
    s_len = len(s)
    row = math.floor(math.sqrt(s_len))
    col = math.ceil(math.sqrt(s_len))

    if row * col < s_len:
        row += 1

    #print(s_len, row, col)

    all_list = []
    string = ""

    index = 0
    for i in range(0, row):
        l = []
        i = 0
        while i < col:
            if index < s_len:
                l.append(s[index])
            else:
                l.append("")
            i += 1
            index += 1
        all_list.append(l)

    #print(all_list)
    for i in range(0, col):
        for j in range(0, row):
            string += all_list[j][i]
        string += " "

    return string


print(encryption("chillout"))