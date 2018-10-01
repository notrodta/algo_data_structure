# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.



'''

ex: array: ["aba","baba","aba","xyz"]
    queries: ["aba", "xyz", "ab"]

    returns: [2,1,0]

'''
def matchingStrings(strings, queries):
    string_freq = {}
    l = []

    for s in strings:
        if s not in string_freq:
            string_freq[s] = 0
        string_freq[s] += 1

    for q in queries:
        if q in string_freq:
            l.append(string_freq[q])
        else:
            l.append(0)

    return l