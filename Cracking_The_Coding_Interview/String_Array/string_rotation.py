# StringRotation:Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of" erbottlewat").


def isSubstring(str1, str2):
    if len(str1) >= len(str2):
        long = str1
        short = str2
    else:
        long = str2
        short = str1

    if short in long:
        return True

    return False

def answer(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = str1+str1

    if isSubstring(str1, str2):
        return True
    else:
        return False



print(answer("waterbottle", "erbottlewat"))
print(answer("waterbottle", "rbottlewati"))