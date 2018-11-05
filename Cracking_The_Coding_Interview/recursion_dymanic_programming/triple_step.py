# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.


# similar to fib time complexity
# O(3^n) or O(branches ^ depth) without memo  , where n is the depth of recursive tree  (https://www.youtube.com/watch?v=NyV0d5QadWM)
# O(mn) with memo, where n is step and m is how many diff steps u can take (length of l)
def answer(n, memo):

    if n < 0 :
        return 0
    if n == 0:
        return 1
    if memo[n] is not None:
        return memo[n]

    memo[n] = answer(n-1, memo) + answer(n-2, memo) + answer(n-3, memo)

    return memo[n]

def answer_memo(n):
    memo = [None] * (n+1)
    return answer(n, memo)


print(answer_memo(5))


# similar to the coin change approach
l = [1,2,3]
def test(n):
    memo = [None] * (n+1)
    memo[0] = 0

    return helper(n, memo)

def helper(n, memo):
    if n == 0:
        return 1
    if n < 0:
        return 0

    if memo[n]:
        return memo[n]

    ways = 0
    for i in range(0,len(l)):
        remaining = n - l[i]
        ways += helper(remaining, memo)

    memo[n] = ways

    return ways


print(test(5))



