# implement a function that given an integer number num, it returns the a string representation of the number, comma separated.
#i.e. f(1234) = “1,234”


def answer(n):
    n = str(n)
    s = ""
    counter = 0
    if len(n) % 3 == 0:
        counter = 0
    if len(n) % 3 == 1:
        counter = 2
    if len(n) % 3 == 2:
        counter = 1

    for i in range (0, len(n)):
        s += n[i]
        counter += 1
        if counter % 3 == 0 and i != len(n) - 1:
            s += ","

    return s



print(answer(100000000))
print(answer(10000000))
print(answer(1000000))
print(answer(100000))
print(answer(10000))
print(answer(1000))
print(answer(100))
print(answer(1))



