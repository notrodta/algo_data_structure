# Permutations without Dups: Write a method to compute all permutations of a string of unique characters.

def permutations(string):
    """Create all permutations of a string with non-repeating characters
    """
    permutation_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [permutation_list.append(char + a) for a in permutations(string.replace(char, ""))]
    return permutation_list



#print(unique_char("aabccd"))
#print(get_perm_string("abcd","c"))

#print(permutations("abcd"))


def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

        # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

        # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            #print([m]+p)
            l.append([m] + p)


    return l


def dup(lst):
    dup = permutation(lst)
    s = set()
    for l in no_dup:
        s.add(tuple(l))

    return s


# Driver program to test above function
data = list('abca')
no_dup = permutation(data)
print(no_dup)

print()
dup = dup(data)
print(dup)








