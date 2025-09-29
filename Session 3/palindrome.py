string=input('Enter a string: ')
converted_string= string.lower().replace(" ","").replace(".","").replace(",","")
print("Input string: ",string)
print("Converted string: ",converted_string)

if string == string[::-1]:
    print("IT's a palindrome")
else:
    print("It's not a palindrome")
