# Given an array and integer m, had to find average of m groups in O(n).


def answer(arr, m):
    x = m-1

    for i in range (0, len(arr) - x):
        counter = 0
        num = 0
        while counter < m:
            num += arr[i+counter]
            counter += 1
        print(num/m)



answer([1,2,3,4,5,6,7], 3)

