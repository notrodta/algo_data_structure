'''

ex:
{[()]}
{[(])}
{{[[(())]]}}

answer:
YES
NO
YES

'''


# solution 1
def get_opening_bracket(bracket):
    if bracket == ")":
        return "("
    elif bracket == "}":
        return "{"
    elif bracket == "]":
        return "["
    else:
        return None


def is_matched(expression):
    stack = []

    for bracket in expression:
        stack.append(bracket)
        if len(stack) > 1:
            if stack[-2] == get_opening_bracket(bracket):
                stack.pop()
                stack.pop()

    return len(stack) == 0


# solution 2:
def isMatching(bracket1, bracket2):
    if bracket1 == "{" and bracket2 == "}":
        return True
    elif bracket1 == "[" and bracket2 == "]":
        return True
    elif bracket1 == "(" and bracket2 == ")":
        return True

    return False


def isAddToStack(bracket):
    if bracket == "{" or bracket == "[" or bracket == "(":
        return True
    return False


def isBalanced(s):
    s_len = len(s)
    l = []
    for i in range(0, s_len):
        if isAddToStack(s[i]):
            l.append(s[i])
        else:
            if len(l) <= 0:
                return "NO"
            b1 = l.pop()
            b2 = s[i]
            print(b1, b2)
            if isMatching(b1, b2) == False:
                return "NO"

    if len(l) == 0:
        return "YES"
    else:
        return "NO"