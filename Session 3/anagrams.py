string1=input("enter the first string:")
string2=input("enter the second string:")
string1 = string1.lower().replace(" ","")
string2= string2.lower().replace(" ","")
if sorted(string1) == sorted(string2):
    print("they are anagrams")
else:
    print("they are not anagrams")