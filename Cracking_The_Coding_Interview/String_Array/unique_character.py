#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

#only string and arrays are allowed

# solution 1: sorting, and compare neighbor

def answer(str):
    l = []
    for char in str:
        l.append(char)

    l = sorted(l)
    l_len = len(l)
    for i in range(0,l_len-1):
        if l[i] == l[i+1]:
            return False

    return True

# solution 2: using ascii and array
def answer_two(str):
    str_len = len(str)

    if str_len > 128: return False # only 128 unique characters in total

    l = [False] * 128

    for i in range (0, str_len):

        val = ord(str[i])

        if l[val] == True:
            return False
        l[val] = True

    return True








print(answer("asksfjiosem231!sd"))
print(answer("abc!sd"))
print(answer_two("asksfjiosem231!sd"))
print(answer_two("abc!sd"))