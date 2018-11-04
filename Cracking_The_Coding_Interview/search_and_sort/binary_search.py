# logn

# def bs(arr, n):
#     if len(arr) == 0:
#         return False
#     if len(arr) == 1 and arr[0] != n:
#         return False
#
#     mid = len(arr) // 2
#
#     if arr[mid] == n:
#         return True
#     elif arr[mid] > n:
#         return bs(arr[:mid],n)
#     else:
#         return bs(arr[mid+1:], n)


def bs(arr, val):
    return bs_helper(arr, 0, len(arr)-1, val)

def bs_helper(arr, l, r, val):

    if r >= l:
        mid = (r+l)//2  #l + (r - l) // 2 <-- this also works

        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            return bs_helper(arr, l, mid-1, val)
        else:
            return bs_helper(arr, mid+1, r, val)
    else:
        return -1


l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4,5,6,7,8]

print(bs(l1,5))
print(bs(l1,1))
print(bs(l1,10))
print(bs(l2,5))
print(bs(l2,1))
print(bs(l2,10))
# True
# True
# False
# True
# True
# False
