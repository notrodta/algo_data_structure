# Permutations without Dups: Write a method to compute all permutations of a string of unique characters.

def permutations(string):
    """Create all permutations of a string with non-repeating characters
    """
    permutation_list = []
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return string
    else:
        for char in string:
            #[permutation_list.append(char + a) for a in permutations(string.replace(char, ""))]
            for a in permutations(string.replace(char, "")):
                permutation_list.append(char + a)
    return permutation_list


print(permutations(""))
print(permutations("abca"))
print(permutations("abc"))



# permutation without all chars, not with only unique chars
def permutations2_helper(string):
    """Create all permutations of a string with non-repeating characters
    """
    permutation_list = []
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [permutation_list.append(char + a) for a in permutations(string)]
    return permutation_list

def permutations2(string):
    s = set()
    perm = permutations2_helper(string)

    for p in perm:
        s.add(p)
    return s


print()
print(permutations2_helper("abca"))
print()
print(permutations2("abca"))



''' --------------------------- Better one!! -----------------------------'''

# permutation without unique characters
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return ""

        # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return lst

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
            l.append(m + p)

    return l


def dup(lst):
    s = set()
    perm = permutation(lst)

    for p in perm:
        s.add(p)

    return s



print()
print(permutation("abc"))
print(dup("abca"))









