list_of_tuples = [('Alice', 25), ('Bob',30), ('charlie', 20)]

#descending order
sorted_list = sorted(list_of_tuples, key=lambda x: x[1], reverse=True)

print("Sorted List: ",sorted_list)