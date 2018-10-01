# this is how to change variable values outside of functions using global keyword

t = False
def test1():
    global t
    t = True
    print(t)


def test():
    test1()
    print(t)

test()