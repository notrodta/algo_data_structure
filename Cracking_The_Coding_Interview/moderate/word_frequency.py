# 16.2 Word Frequencies: Design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?


def answer(s):
    s = s.split()
    word_freq = {}

    for word in s:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1

    return word_freq


print(answer("The documentation generators should be properly installed on your machine. Refer to their respective download and installation pages for details. The"))
