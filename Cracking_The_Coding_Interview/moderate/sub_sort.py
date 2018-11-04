# 16.16 Sub Sort: Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n , the entire array would be sorted. Minimize n such sequence).


# newer way of doing it, more clean than the old way
import sys
def alt(arr):
    left,right = None, None

    smallest = sys.maxsize
    for i in range (0, len(arr)-1):
        if arr[i] > arr[i+1]:
            smallest = min(arr[i:])
            break

    left = correct_index_left(arr, smallest)

    largest = -sys.maxsize-1
    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            largest = max(arr[0:i+1])
            break

    right = correct_index_right(arr, largest)

    return (left,right)

def correct_index_left(arr, val):
    for i in range (0, len(arr)):
        if val < arr[i]:
            return i
    return -1

def correct_index_right(arr, val):
    for i in range(len(arr)-1, -1, -1):
        if val > arr[i]:
            return i
    return -1



'''         OLD WAY         '''

def get_index(arr, val): # this can be furthur optimized
    for i in range(0, len(arr)):
        if arr[i] == val:
            print("index of mini/maxi:", i)
            return i


def helper(arr, index, val, is_left):
    arr_len = len(arr)

    if is_left:
        for i in range (0, index):
            if val < arr[i]:
                return i
    else:
        for i in range (index, arr_len):
            if val < arr[i]:
                return i-1
    return arr_len-1


def answer(arr):
    left,right = None,None
    left_index, right_index = None, None


    i = 1
    arr_len = len(arr)

    while i < arr_len-1:
        if arr[i] < arr[i-1]:
            left = i
            break
        i += 1

    mini = min(arr[left:])
    print("mini:", mini)
    left_index = helper(arr, get_index(arr, mini), mini, True)
    print("left index:",left_index)
    print()

    i = arr_len - 2
    while i > 0:
        if arr[i] > arr[i+1]:
            right = i
            break
        i -= 1

    maxi = max(arr[:right+1])
    print("maxi:",maxi)

    right_index = helper(arr, get_index(arr, maxi), maxi, False)
    print("right index:",right_index)

    print()

    return (left_index,right_index)


l = [1,2,4,7,10,11,7,12,6,7,16,18,19]

print(answer(l))
print(alt(l))




