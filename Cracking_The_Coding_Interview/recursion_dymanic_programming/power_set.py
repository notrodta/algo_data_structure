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


#print(answer([1,2,3],[]))
#print()


# https://www.youtube.com/watch?v=J_odcqzHGqw
#recursion:
# expnential time complexity?
def powerset(set, newset):
    #print(which)
    if set == []:
        #print("returning:", "set", set, "newset",newset)
        #print(newset)
        return [newset]

    #print("b4", "set",set, "newset",newset)

    res = []
    for s in powerset(set[1:], newset + [set[0]]):
        res.append(s)
        # print("first", "set:", set, "newset:", newset, "s:", s, "res:",res)
        # print("second set start with", "set:", set, "newset:", newset,)
        # print()
    for s in powerset(set[1:], newset):
        res.append(s)
       # print("second", "set:", set, "newset:", newset ,"s:", s, "res", res)

    return res

print()
print(powerset([1,2,3],[]))
# [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]



# https://www.youtube.com/watch?v=J_odcqzHGqw
def sublist(set):
    a = []
    sublist_helper(set, a, chosen=[])
    return a

def sublist_helper(set,a,chosen):
    if len(set) == 0:
        a.append(chosen[:])
        #print(chosen)
    else:
        # there are two choices to explore
        # the subset with the first element, and the one without it
        first = set[0]
        set.pop(0)

        chosen.append(first)            # choose/explore (with)
        sublist_helper(set, a, chosen)

        chosen.pop(len(chosen)-1)       # choose/explore without
        sublist_helper(set,a, chosen)

        set.insert(0,first)            # un-choose


print(sublist([1,2,3]))



