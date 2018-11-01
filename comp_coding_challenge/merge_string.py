def create_list(a,b,l,shortest,rem):
    for i in range(0,shortest):
        l.append(a[i])
        l.append(b[i])
    l.extend(rem)

def merge_string(a,b):
    len_a = len(a)
    len_b = len(b)
    l = []
    if len_a < len_b:
        shortest = len_a
        create_list(a,b,l,shortest,b[shortest:])
    else:
        shortest = len_b
        create_list(a, b, l, shortest, a[shortest:])

    return "".join(l)


print(merge_string("abc","defghi"))
