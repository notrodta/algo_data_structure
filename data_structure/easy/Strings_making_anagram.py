'''
Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of
each other if the first string's letters can be rearranged to form the second string. In other words, both strings must
contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams,
but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number
of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions
 required to make  and  anagrams. Any characters can be deleted from either of the strings.
'''


def number_needed(a, b):
    if len(a) < len(b):
        small = list(a)
        large = list(b)
    else:
        small = list(b)
        large = list(a)

    l = []

    x = 0
    count = 0
    while len(small) - 1 >= x:
        found = False
        for i in range(0, len(large)):
            #print(small[x], large[i])
            if small[x] == large[i]:
                large.pop(i)
                l.append(small.pop(x))
                count += 1
                found = True
                break
        if found is False:
            x += 1

    print(l)
    counter = len(a) - count
    counter += len(b) - count

    return counter

print(number_needed("cde","abc"))

