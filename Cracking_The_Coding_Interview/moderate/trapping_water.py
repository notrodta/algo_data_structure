# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# https://www.geeksforgeeks.org/trapping-rain-water/

arr1 = [3,0,0,2,0,4]
arr2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
arr3 = [3,0,0,2,0,4,0,0,0,0,3]

def answer(arr):
    n = len(arr)
    left = [0] * n
    right = [0] * n

    water = 0

    # fill left array 
    left[0] = arr[0]
    for i in range(1,n):
        left[i] = max(left[i-1], arr[i])

    # fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    print(left)
    print(right)

    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0,n):
        print(arr[i] ,min(left[i], right[i]) ,min(left[i], right[i]) - arr[i] )
        water += min(left[i], right[i]) - arr[i]

    return water


# print(answer(arr1))
# print(answer(arr2))
print(answer(arr3))








