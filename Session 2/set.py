#creating a set

Set={1,2,3,4,5}

#Adding element is set
Set.add(8)
print("After adding element: ",Set)

#Removing element is the set
Set.remove(1)
print("After removing element: ",Set)

#checking membership
print("IS 4 in the set?", 4 in Set)

#Creating another set
anotherset={4,5,6,8}

#Union of set
union_set= Set.union(anotherset)
print("Union of sets: ",union_set)

#Intersection
intersection_set= Set.intersection(anotherset)
print("Intersection : ",intersection_set )

#Difference

difference_set= Set.difference(anotherset)
print("Difference : ",difference_set)

#Checking if a set is a subset
print("Is {4,5} is a subset of the set? ", {4,5}.issubset(Set))
