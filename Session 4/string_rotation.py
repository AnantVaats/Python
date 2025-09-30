string1 = input('Enter the first string: ')
string2 = input('Enter the second string: ')

if len(string1) != len(string2):
    print("No the strings are not rotations of each other")

else:
    if string1 in (string2+string2):
        print("Yes, one string is a rotation of the other.")
    else:
        print("No, the strings are not rotations of each other.")

