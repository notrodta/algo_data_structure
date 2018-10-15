# reverse sentence


def answer(n):
    n = n.replace(",", " ,")
    n = n.split()
    s = ""

    for i in range (len(n)-1, -1 ,-1):
        s += n[i] + " "
    return s


print(answer("hello world, my name is rod"))