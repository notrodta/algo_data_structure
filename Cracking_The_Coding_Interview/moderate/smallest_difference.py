
import sys

def answer(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    smallest = sys.maxsize

    print(arr1)
    print(arr2)

    x,y = 0,0

    i,j = 0,0,

    while True:
        print(arr1[i], arr2[j])
        val = abs(arr1[i] - arr2[j])

        if val < smallest:
            smallest = val
            x,y = arr1[i], arr2[j]

        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

        if i > len(arr1)-1 or j > len(arr2)-1:
            break

    return x,y,smallest


arr1 = [23,42,11,26]
arr2 = [2,8,12,18]
print(answer(arr1, arr2))