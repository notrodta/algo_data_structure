# Pattern Matching: You are given two strings, pattern and value. The pattern string consists of just the letters a and b, describing a pattern within a string. For example, the string catcatgocatgo matches the pattern aabab (where cat is a and go is b). It also matches patterns like a, ab, and b. Write a method to determine if value matches pattern.


def answer(pattern, value):
    if len(pattern) == 1: return True
    if len(pattern) == 2 and len(value) >= 2: return True

    a_len = 1

    while a_len < len(value)-1:
        #new_value = value.replace(value[:a_len],"")
        #print(value[:a_len], new_value)
        offset = helper(a_len, pattern, value)
        # print(value[:a_len], value[a_len: a_len+offset])
        # print()
        if offset < 0: return False
        if check(value[:a_len], value[a_len: a_len+offset], pattern, value):
            return True

        a_len += 1

    return False

def helper(a_len, pattern, value):
    a_counter = 0
    b_counter = 0
    for char in pattern:
        if char == 'a':
            a_counter += 1
        else:
            b_counter += 1

    val_len = len(value)
    a = val_len - (a_counter * a_len)
    #print("a", a, "b_len", a//b_counter)
    return a//b_counter


def check(a,b, pattern, value):
    s = ""

    for char in pattern:
        if char == 'a': s += a
        else: s += b

    return s == value



# print(check('dog', 'cat', 'aba', 'dogcatdog'))
print(answer('aba','dogcatdog'))
print(answer('aba','dogcatdogs'))
print(answer('ab','dogcatdog'))
print(answer('b','dogcatdog'))