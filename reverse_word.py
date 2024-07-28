str = input('write any sentence: ')
word = str.split()

reverse_word = ' '.join(word[::-1])
print(reverse_word)

# alternative
def reverse_word(sentence):
    word_1 = sentence.split()
    word_1.reverse()
    return ' '.join(word_1)

sent = input('write your sentence: ')
print(reverse_word(sent))

