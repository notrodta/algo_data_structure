#One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

#EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false


# use dict, get count from one word (longer one)
# - count from the other word

# if couonter > 1; false

# if 1 word is shorter than the other, check if dict has only 1 char with 1 word left, every counter on other char should be 0, also use counter thing from the next step
# if both words are even, use a variable to store a counter of how many chars not in the first word, if counter > 1, then no good, and also check that the dic only has 1 char with counter = 1


# get the long str and short str
def helper(str1, str2):
    if len(str1) >= len(str2):
        return [str1, str2]

    return[str2, str1]

def answer(str1, str2):
    long = helper(str1, str2)[0]
    short = helper(str1,str2)[1]
    counter = 0

    char_freq = {}

    for char in long:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    for char in short:
        if char not in char_freq:
            counter += 1
            if counter > 1:
                return False
        else:
            char_freq[char] -= 1

    counter2 = 0
    for key, value in char_freq.items():
        if value == 1:
            counter2 += 1
        if value > 1 or counter2 > 1:
            return False


    return True

#EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false

print(answer("pale","ple"))
print(answer("pales","pale"))
print(answer("pale","bale"))
print(answer("pale","bae"))