def fact(n):
    if n == 0:
        return 1

    return n * fact(n-1)

print(fact(3))

def power(base, e):
    if e == 0:
        return 1

    return base * power(base, e-1)

print(power(2,4))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

print(fib(8))


dict = {}
dict[0] = 0
dict[1] = 1
def fib_dp(n):
    if dict.get(n) is None:
        dict[n] = fib_dp(n-1) + fib_dp(n-2)

    return dict[n]

print(fib_dp(14))


def reverse_string(s):
    if s == "":
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("rodta"))

def r(s):
    if s == "":
        return s

    return s[-1] + r(s[:-1])


print(r("rodta"))


def sumofdigits(num):
    if str(num) == "":
        return 0

    return int(str(num)[0]) + int(sumofdigits(str(num)[1:]))

print(sumofdigits(12353))


def fact1(n):
    if n == 0:
        return 1

    return n * fact1(n-1)

print(fact1(3))

def ex(b,e):
    if e == 0:
        return 1

    return b * ex(b,e-1)

print(ex(2,4))

f = {}
f[0] = 0
f[1] = 1
def fibdp(n):
    if f.get(n) is None:
        f[n] = fibdp(n-1) + fibdp(n-2)

    return f[n]

print(fibdp(14))


def reverse_string(s):
    if s == "":
        return s

    return s[-1] + reverse_string(s[:-1])

print(reverse_string("rodta"))



def t(n):
    if n == 1:
        return 1

    return t(n-1)

print(t(5))