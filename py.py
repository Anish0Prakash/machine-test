import copy
List1 = [[1, 2, 3], [5, 6, 7], [7, 8, 9]]
List2_shallow = List1.copy()
List2_deep = copy.deepcopy(List1)
print("Original List (List1):", List1)
print("Shallow Copy (List2_shallow):", List2_shallow)
print("Deep Copy (List2_deep):", List2_deep)
List1[0][0] = 100
print("\nAfter modifying List1:")
print("Original List (List1):", List1)
print("Shallow Copy (List2_shallow):", List2_shallow)  
print("Deep Copy (List2_deep):", List2_deep) 
