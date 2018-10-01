# String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def answer(_str):
    str_len = len(_str)
    s = _str[0]
    counter = 0

    for i in range (0, str_len-1):
        counter += 1

        if _str[i] != _str[i+1]:
            s += str(counter)
            s += _str[i+1]
            counter = 0

    counter += 1
    if _str[-1] == _str[-2]:
        s += str(counter)
    else:
        s += str(counter)

    return s

#a2blc5a3
print(answer("aabcccccaaa"))
print(answer("aabcccccaaab"))
print(answer("aabcccccaaabb"))


