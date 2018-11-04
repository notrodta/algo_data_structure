# 16.24 Pairs with Sum: Design an algorithm to find all pairs of integers within an array which sum to a specified value.


def using_hash(arr, sum):
    s = set(arr)

    l = set()
    for val in s:
        diff = sum - val
        if diff in s:
            if val > diff:
                big, small = val, diff
            else:
                big,small = diff, val
            l.add( (small,big) )
    return l


l = [-2,-1,0,3,5,6,7,9,13,14]
print(using_hash(l, 8))



# using two pointers, 1 beginning and 1 at the end, increment toward each other based on conditions
def no_hash(arr, sum):
    arr = sorted(arr)

    front = 0
    back = len(arr)-1

    l = set()

    while (front != back):
        diff = arr[front] + arr[back]
        if diff > sum:
            back -= 1
        elif diff == sum:
            l.add( (arr[front], arr[back]) )
            front += 1
        elif diff < sum:
            front += 1

    return l


print(no_hash(l,8))
