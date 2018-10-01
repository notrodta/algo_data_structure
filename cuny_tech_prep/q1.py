'''

giving a string of words separated by spaces
find longest even length word

'''


a = "hello my name is rod namename pesddwsd"
b = "to000"

def GetLongestEvenWord(a):
    max_len_even_word = ""

    for word in a.split():
        if len(word) % 2 == 0:
            if len(word) > len(max_len_even_word):
                max_len_even_word = word

    if len(max_len_even_word) > 0:
        return max_len_even_word
    else:
        return "00"
    #     if len(word) > len(max_len_word):
    #         max_len_word = word
    # return max_len_word


print(GetLongestEvenWord(a))
print(GetLongestEvenWord(b))