# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

# sorting and compare
def answer(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = sorted(list(str1))
    str2 = sorted(list(str2))

    print(str1)
    print(str2)

    for i in range (0, len(str1)):
        if str1[i] != str2[i]:
            return False

    return True



print(answer("dog", "god"))
