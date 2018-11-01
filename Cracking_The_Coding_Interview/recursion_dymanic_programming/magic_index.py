# Magic Index: A magic index in an array A[ 1.•.n-1] is defined to be an index such that A[i] = i
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
# FOLLOW UP
# What if the values are not distinct?


# binary search method, O(log n)
def answer(arr, index=None):
    #print()
    i = len(arr)//2
    #print(i)

    if index == None:
        index = i

    if len(arr) == 0:
        return False
    if arr[i] == index:
        return True

    #print(arr)
    #print("indeax:",index)
    #print("value:",arr[i])


    if index > arr[i]:
        #print("more")
        new_index = len(arr[i+1:])//2 + index + 1
        return answer(arr[i+1:], new_index)
    elif index < arr[i]:
        #print("less")

        # the new_index is calculated differently based on if the length of hte array is even or odd here
        if len(arr[:i]) % 2 == 0:
            new_index = index - len(arr[:i])//2
        else:
            new_index = index - len(arr[:i])//2 - 1
        return answer(arr[:i], new_index)


arr = [-40,-20,-1,1,2,3,5,8,9,12,13]
arr2 = [-40,-20,-1,1,2,3,5,7,9,12,13]
arr3 = [0,1,5,6,7,8,9,10,11]
arr4 = [-1,0,2,6,7,8,9,10,11,13]
arr5 = [-1,0,3,6,7,8,9,10,11,13]
print(answer(arr))
print(answer(arr2))
print(answer(arr3))
print(answer(arr4))
print(answer(arr5))


