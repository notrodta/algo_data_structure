# minimum amt of coins to make n cents from list of arr

import sys

def minCoins(coins, n, memo):
    if n == 0:
        return 0
    if n <0:
        return 0

    res = sys.maxsize

    if memo[n] != sys.maxsize:
        return memo[n]

    for i in range(0,len(coins)):
        if coins[i] <= n:
            memo[n] = minCoins(coins, n-coins[i], memo)

            if memo[n] != sys.maxsize and memo[n] + 1 < res:
                res = memo[n] + 1

    return res


def answer(coins, n):
    l = [sys.maxsize] * (n+1)
    l[0] = 0

    return minCoins(coins, n, l)



l = [9,6,5,1]
print(answer(l, 11))

l2 = [25,10,5]
print(answer(l2, 30))