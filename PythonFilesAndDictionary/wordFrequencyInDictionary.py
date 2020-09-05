sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

word_counts = word_count(sentence)
print(word_counts)





