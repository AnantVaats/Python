#creating a dictionary
Dict= {'name': 'aman', 'age': 22, 'city': 'Delhi'}

#Accessing elements
print("Name:", Dict['name'])

#Modifying elements

Dict['age']=30

#Adding new key value pair

Dict['gender']='Male'

#Removing key - value pairs
removed_value= Dict.pop('city')

#checking a key exist
print("IS 'name' a key in the dictionary?: ", 'name' in Dict)

#getting key and values
print("Keys: ", Dict.keys())
print("Values: ",Dict.values())

#length of dict
print("length of Dictionary: ",len(Dict))

#creating another dictionary for opeartions
another_dict={'country':'India'}

#Merging dictionary
Dict.update(another_dict)
print("Merged Dictionary: ", Dict)

