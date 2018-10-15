# reverse string

def answer(n):
    s = ""
    for i in range (len(n)-1, -1, -1):
        s += n[i]

    return s


print(answer("hello"))