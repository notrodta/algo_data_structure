# Power Set: Write a method to return all subsets of a set.



# did not use recursion, but did learn about shallow and deep copy. shallow copy is pretty much = sign when used on list.
# deep copy is another copy of the object, what u do to the copy has no effect to the original
# ex: new = subset, new will be a pointer to subset, so whatever you do to new, it will also do to subset, since they are the same
import copy
def answer(set, subsets):
    subsets.append([])

    for s in set:
        for i in range(len(subsets)):
            new_subset = copy.deepcopy(subsets[i])
            new_subset.append(s)
            subsets.append(new_subset)

    return subsets


print(answer([1,2,3],[]))
print()


# https://www.youtube.com/watch?v=J_odcqzHGqw
#recursion:
# expnential time complexity?
def powerset(set, newset):
    if set == []:
        return [newset]

    res = []
    for s in powerset(set[1:], newset + [set[0]]):
        res.append(s)
    for s in powerset(set[1:], newset):
        res.append(s)

    return res

print(powerset([1,2,3],[]))
# [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]



