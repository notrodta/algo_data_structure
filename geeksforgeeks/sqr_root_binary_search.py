# find square root of a number using binary search


def helper(start, end, n):
    if n == 0 or n == 1: return n

    mid = (start + end) // 2

    x = mid * mid

    if x == n: return mid

    if x > n:
        return helper(0, mid, n)

    if x < n:
        return helper(mid, end, n)

def answer(n):
    return helper(0, n, n)


print(answer(64))