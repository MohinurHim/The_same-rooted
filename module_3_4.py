# Однокоренные
def single_root_words(root_word, *other_words):
    same_words = []
    word = root_word.lower()
    for w in other_words:
        word2 = w.lower()
        if word in word2 or word2 in word:
            same_words.append(w)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
