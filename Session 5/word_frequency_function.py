import string
def word_frequency(text):
    text = text.translate(str.maketrans('','',string.punctuation)) # Remove punctuation
    words = text.lower().split()
    frequency ={}
    
    #another way of dictionay add and update
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

print(word_frequency("hello how are you, my way of saying hello."))