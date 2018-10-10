# Coins: Given an infinite number of quarters (25 cents), dimes (1O cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents.

list = [25,10,5,1]
def combo(amt, currentCoin):
    # if amt >= 0:
    #     print(list[currentCoin])

    if amt == 0:
        return 1
    if amt < 0:
        return 0


    nCombos = 0

    for coin in range (currentCoin, len(list)):
        nCombos += combo(amt - list[coin], coin)

    return nCombos

print(combo(20,0))



# this way cosider all permuation as unique answer, similar to the staircase problem
def test(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    return test(n-25) + test(n-10) + test(n-5) + test(n-1)


print(test(20))
