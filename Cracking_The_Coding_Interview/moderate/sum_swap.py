# Sum Swap: Given two arrays of integers,  nd a pair of values (one value from each array) that you can swap to give the two arrays the same sum.

#
# EXAMPLE
# Input: {4, 1, 2, 1, 1, 2} and {3, 6, 3, 3}
# Output: {1, 3}


def answer(set1, set2):
    diff = sum(set1) - sum(set2)

    for val in set1:
        target = abs(diff - val)
        if target in set2:
            return val, target

    return None


s1 = {4, 1, 2, 1, 1, 2}
s2 = {3, 6, 3, 3}

print(answer(s1,s2))

