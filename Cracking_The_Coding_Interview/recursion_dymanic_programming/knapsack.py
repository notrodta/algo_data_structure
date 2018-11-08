# https://www.youtube.com/watch?v=xOlhR_2QCXY


weight = [1,2,4,2,5]
value = [5,3,5,3,2]

# O(2^n) without memo
def ans(capacity, n):
    #print(n)
    if n == 0 or capacity == 0:
        return 0
    if weight[n-1] > capacity:
        return ans(capacity, n-1)
    else:
        temp1 = ans(capacity, n-1)
        temp2 = value[n-1] + ans(capacity - weight[n-1], n-1)
        result = max(temp1, temp2)
        #print("without:",temp1, "with:",temp2)
        return result



print(ans(10,5))



wt = [1,2,4,2,5]
val = [5,3,5,3,2]


def knapSack(W,n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n - 1] > W):
        return knapSack(W,  n - 1)

        # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        temp1 = knapSack(W, n - 1)
        temp2 = val[n - 1] + knapSack(W - wt[n - 1], n - 1)
        return max(temp1, temp2)


print(knapSack(10, 5))