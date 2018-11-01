# Contiguous Sequence: You are given an array of integers (both positive and negative). Find the contiguous sequence with the largest sum. Return the sum.

import sys

def answer(arr):
    curr_sum, max_sum = 0, -sys.maxsize

    arr_len = len(arr)
    for i in range(0, arr_len):
        curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


arr = [2,-8,3,-2,4,-10]
print(answer(arr))
