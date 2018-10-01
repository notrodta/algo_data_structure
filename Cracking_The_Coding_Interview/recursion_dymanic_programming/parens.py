# Parens: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n pairs of parentheses.


# bottom up approach
# reference: https://www.youtube.com/watch?v=vYquumk4nWw


# WRONG =[
def answer(n):
    if n == 0: return
    if n == 1: return ["()"]

    bottom_up = [None] * (n+1)
    bottom_up[0] = []
    bottom_up[1] = ["()"]


    for i in range(2, n+1):
        s = set()
        #for j in range (0, len(bottom_up[i-1])):
        for data in bottom_up[i-1]:
            curr = data
            data1 = "(" + curr + ")"
            data2 = "()" + curr
            data3 = curr + "()"
            s.add(data1)
            s.add(data2)
            s.add(data3)
        bottom_up[i] = s

    print()
    print(len(bottom_up[n]))
    return bottom_up[n]


print(answer(1))
print(answer(2))
print(answer(3))
print(answer(4))
print(answer(5))


# Python3 program to
# Print all combinations
# of balanced parentheses

# Wrapper over _printParenthesis()
def printParenthesis(str, n):
    if (n > 0):
        _printParenthesis(str, 0,
                          n, 0, 0)
    return


def _printParenthesis(str, pos, n,
                      open, close):
    if (close == n):
        for i in str:
            print(i, end="")
        print()
        return
    else:
        if (open > close):
            str[pos] = ')'
            _printParenthesis(str, pos + 1, n,
                              open, close + 1)
        if (open < n):
            str[pos] = '('
            _printParenthesis(str, pos + 1, n,
                              open + 1, close)

            # Driver Code


n = 5
str = [""] * 2 * n
printParenthesis(str, n)


