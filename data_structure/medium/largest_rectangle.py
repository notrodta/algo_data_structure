# Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

#https://www.hackerrank.com/challenges/largest-rectangle/problem

def largestRectangle(h):
    i = 0
    largest = 0
    h_len = len(h)

    while i < h_len:
        front = 1
        back = -1
        counter = 1
        while i + back >= 0:
            if h[i + back] >= h[i]:
                print(h[i], h[i + back])
                back -= 1
                counter += 1
            else:
                break
        while i + front < h_len:
            if h[i + front] >= h[i]:
                print(h[i], h[i + front])
                front += 1
                counter += 1
            else:
                break

        num = h[i] * counter
        if num > largest:
            largest = num

        i += 1

    return largest