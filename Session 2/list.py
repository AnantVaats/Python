#creating a list
L=[1,'hello', {}, 'world', 5]

#accessing the elements

print("First element: ", L[0])

#slicing
print("Slice: " ,L[1:3])

#Appending
L.append(True)

#Inserting
L.insert(2,"good morning")
print("Inserting: ",L)

#Removing
L.remove(5)
print("Removed: ", L)

#Popping => remove the last index value
item=L.pop()
print("Popped item: ",item)
print("Remaing: ",L)

#length of list
print("Length of list: ",len(L))

#deleting by index
del L[0]
print(L)
