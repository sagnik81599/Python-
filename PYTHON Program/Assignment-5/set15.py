set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common_elements = set1.intersection(set2)

if common_elements:
    print("Common elements:", common_elements)
    for element in common_elements:
     print(element)
else:
    print("No common elements")

