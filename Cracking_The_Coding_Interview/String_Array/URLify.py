#URLi : Write a method to replace all spaces in a string with '%20  You may assume that the string has suf cient space at the end to hold the additional characters, and that you are given the "true" length of the string.

# making a second string
def answer(str):
    s = ""

    for char in str:
        if char == " ":
            s = s + "%20"
        else:
            s = s + char

    return s


# working backwards, using array, create enought spaces for array with len of new string after replacing spaces
def answer_two(str):
    counter = 0

    for char in str:
        if char == " ":
            counter += 1

    l = [""] * (len(str) + counter * 2)
    index = len(l) - 1

    for i in range(len(str) - 1, -1, -1):
        char = str[i]
        if char == " ":
            l[index] = "0"
            l[index - 1] = "2"
            l[index - 2] = "%"
            index -= 3
        else:
            l[index] = char
            index -= 1


    return "".join(l)

print(answer("hello world, my name is Rod"))
print(answer_two("hello world, my name is Rod"))