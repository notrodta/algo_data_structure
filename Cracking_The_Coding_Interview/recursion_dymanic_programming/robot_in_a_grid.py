# Robot in a Grid: Imagine a robot sitting on the upper le  corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.


# recursion, with memo
def answer(r,c,n,m, memo):
    if r == n and c == m:
        return 1
    if r > n or c > m:
        return 0
    if memo[r][c] > -1:
        return memo[r][c]

    memo[r][c] = answer(r+1,c, n,m, memo) + answer(r,c+1,n,m, memo)
    return memo[r][c]


def answer_memo(n,m):
    memo = [[-1 for i in range(m+1)] for j in range(n+1) ]
    return answer(1,1,n,m,memo)



print(answer_memo(7,3))



