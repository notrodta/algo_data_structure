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


def perm1(string):
    print("perm")
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return [string]
    else:
        l = []
        for i in range(len(string)):
            x = string[i]
            xs = string[:i] + string[i+1:]
            for p in perm1(xs):
                l.append([x] + p)
            return l

data = list('abcd')
print(perm1(data))






#print(unique_char("aabccd"))
#print(get_perm_string("abcd","c"))

print(permutations("abcd"))


