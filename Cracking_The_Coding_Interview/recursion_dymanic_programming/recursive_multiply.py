# Recursive Multiply: Write a recursive function to multiply two positive integers without using the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.



def answer(x,y):
    big = x if x>=y else y
    small = x if x < y else y

    if y == 0:
        return 0

    return big + answer(big, small-1)


print(answer(4,9))
print(answer(5,8))
