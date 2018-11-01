# 16.24 Pairs with Sum: Design an algorithm to find all pairs of integers within an array which sum to a specified value.


def using_hash(arr, sum):
    arr = set(arr)

    l = []


    for val in arr:
        diff = sum-val
        print(val, diff)
        if diff in arr:
            l.append({val,diff})

    return l


l = [-2.-1,0,3,5,6,7,9,13,14]
print(using_hash(l, 8))