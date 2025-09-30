paragraph = "hadoop hive sark\n spark spark hive\n kafka spark"
words = paragraph.split()
word_freq = {}
for word in words:
    word = word.lower()
    #addding new key and updating value
    word_freq[word] = word_freq.get(word,0)+1
sorted_word_freq = sorted(word_freq.items(), key = lambda x: x[1], reverse=True)
for word,freq in sorted_word_freq:
    print(f"{word}: {freq}")