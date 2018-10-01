# Power Set: Write a method to return all subsets of a set.



# did not use recursion, but did learn about shallow and deep copy. shallow copy is pretty much = sign when used on list.
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
