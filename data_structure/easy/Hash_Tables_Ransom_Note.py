'''

A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants to know if
he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his
note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or
concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note
exactly using whole words from the magazine; otherwise, print No.


ex:
magazine: give me one grand today night
ransom: give one grand today

answer: yes

'''



# solution 1
from collections import Counter


def ransom_note1(magazine, rasom):
    return (Counter(rasom) - Counter(magazine)) == {}


# solution 2
from collections import defaultdict


def ransom_note2(magazine, ransom):
    d = defaultdict(int)

    for word in magazine:
        d[word] += 1
    for word in ransom:
        if d[word] == 0:
            return False
        d[word] -= 1

    return True
