
#0,1,1,2,3,5,8,13,21,34
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


print(fib(6))


#bttom up approach
def bu(n):
    memo = [None] * (n+1)
    memo[0] = 0
    memo[1] = 1

    return helper(n, memo)

def helper(n, memo):
    for i in range (2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


print(bu(8))