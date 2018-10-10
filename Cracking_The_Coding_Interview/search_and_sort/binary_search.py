# logn

def bs(arr, n):
    if len(arr) == 0:
        return False
    if len(arr) == 1 and arr[0] != n:
        return False

    mid = len(arr) // 2

    if arr[mid] == n:
        return True
    elif arr[mid] > n:
        return bs(arr[:mid],n)
    else:
        return bs(arr[mid+1:], n)


l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4,5,6,7,8]

print(bs(l1,5))
print(bs(l1,1))
print(bs(l1,10))
print(bs(l2,5))
print(bs(l2,1))
print(bs(l2,10))