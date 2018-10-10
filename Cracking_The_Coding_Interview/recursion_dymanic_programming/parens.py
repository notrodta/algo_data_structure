# Parens: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n pairs of parentheses.


# bottom up approach
# reference: https://www.youtube.com/watch?v=vYquumk4nWw


# https://www.youtube.com/watch?v=LxwiwlUDOk4
def generate_parens(n):
    if n == 0: return []

    return generate_parens_helper("", n, 0)


def generate_parens_helper(curr, open_amt, close_amt):
    if open_amt == 0:
        return [curr + ")" * close_amt]
    if open_amt > 0 and close_amt == 0:
        return generate_parens_helper(curr + "(", open_amt-1, close_amt + 1)

    return generate_parens_helper(curr + "(", open_amt-1, close_amt + 1) \
           + generate_parens_helper(curr + ")", open_amt, close_amt - 1)





# print(generate_parens(1))
# print(generate_parens(2))
print(generate_parens(3))
#print(generate_parens(4))
# print(generate_parens(5))


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


# n = 5
# str = [""] * 2 * n
#printParenthesis(str, n)


