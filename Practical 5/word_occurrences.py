word_count = {}
text = str(input("Type in a sentence: "))

words = text.split()

for word in words:
    times_used = word_count.get(word, 0)
    word_count[word] = times_used + 1

words = list(word_count.keys())
words.sort()


for word in words:
    print("{} : {}".format(word, word_count[word]))