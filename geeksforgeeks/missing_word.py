# find missing word

def answer(s1, s2):
    my_dict = {}

    l = []

    for word in s1.split():
        if word not in my_dict:
            my_dict[word] = 0
        my_dict[word] += 1

    for word in s2.split():
        if word not in my_dict:
            l.append(word)
        if my_dict[word] == 0:
            l.append(word)
        if my_dict[word] > 0:
            my_dict[word] -= 1

    for key, values in my_dict.items():
        if values > 0:
            l.append(key)

    return l

print(answer("hello my name is rod", "hello my name"))

print(answer("This is an example", "is example"))
