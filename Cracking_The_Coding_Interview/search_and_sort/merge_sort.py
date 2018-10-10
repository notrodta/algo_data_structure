
# n log n
def merge(a,b):
    c = []
    a_curr, b_curr = 0,0

    while a_curr < len(a) and b_curr < len(b):
        if a[a_curr] <= b[b_curr]:
            c.append(a[a_curr])
            a_curr += 1
        else:
            c.append(b[b_curr])
            b_curr += 1

    if a_curr == len(a): c.extend(b[b_curr:])
    else: c.extend(a[a_curr:])

    return c


def mergesort(a):
    if len(a) == 1:
        return a

    left,right = mergesort(a[:len(a)//2]), mergesort(a[len(a)//2:])

    return merge(left, right)



l = [2,5,9,7,5,1,23,-4,4]
print(mergesort(l))