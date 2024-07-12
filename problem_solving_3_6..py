# Define the lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 7, 8]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Find intersection of sets (common elements)
common_elements = set1 & set2 & set3

# Find union of all sets (all elements)
all_elements = set1 | set2 | set3

# Unique elements (elements not in common)
unique_elements = all_elements - common_elements

# Convert unique_elements back to a list (if needed)
unique_list = list(unique_elements)

# Print the result
print(unique_list)
