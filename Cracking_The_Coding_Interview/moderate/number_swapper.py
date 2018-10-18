# Number Swapper: Write a function to swap a number in place (that is, without temporary variables).

def swap(a,b):
    a = abs(a - b)
    b = a + b
    a = b - a
    return a, b

print(swap(9,4))

def bit_manipulation(a,b):
    a = a ^ b # xor
    b = a ^ b
    a = a ^ b
    return a, b

print(bit_manipulation(9,4))
