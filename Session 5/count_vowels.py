def count_vowels(S):
    vowels ='aeiouAEIOU'
    count=0
    for char in S:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello"))