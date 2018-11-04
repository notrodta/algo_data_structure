
# time complexity is 2^n, more precisely, golden ratio^n or 1.6... ^ n
# with memo, its n

def f(n, memo):
    if n == 0: return 0
    elif n == 1: return 1

    if memo[n]: return memo[n]

    memo[n] = fib(n-1)+fib(n-2)

    return memo[n]


def fib(n):
    memo = [None] * (n+1)
    memo[0] = 0

    return f(n, memo)


print(fib(5))