squares = [ x ** 2 for x in range(1,11)]
print("Squaares of number 1 to 10: ", squares)

#even numbers
even = [ x  for x in range(1,21) if x % 2 ==0]
print("Even numbers 1 to 20: ", even)

uppercase_letters=[chr(x) for x in range(ord('A'),ord('Z')+1)]
print("Uppercase letters from A to Z: ",uppercase_letters)

#vowel counter
sentence = "The quick brown fox jumps over the lazy dog"
word_vowel_counts=[sum(1 for char in word if char.lower() in 'aeiou') for word in sentence.split()]
print("Counts of vowel in each word: ",word_vowel_counts)


