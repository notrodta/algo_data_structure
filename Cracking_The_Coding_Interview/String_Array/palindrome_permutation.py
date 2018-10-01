# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.


# tac o cat

# tac cat

# aa aa
# aa a aa

def answer(str):
    str = str.replace(" ", "")
    str = str.lower()
    str_len = len(str)

    char_freq = {}

    counter = 0

    for char in str:
        if char != " ":
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1

    print()
    print(char_freq)

    for key, value in char_freq.items():
        if str_len % 2 == 0:
            if value % 2 != 0:
                return False
        else:
            if value % 2 != 0:
                counter += 1

            if counter > 1:
                return False

    print(counter)


    return True


print(answer("Tact Coa"))
print(answer("Tact Coaa"))