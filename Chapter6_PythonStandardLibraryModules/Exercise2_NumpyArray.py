import numpy as np

# Given array
a = np.array([20, 23, 82, 40, 32, 15, 67, 52])

# Find the indices of even numbers
# ill append the index numbers of all the even numbers
even_indices = []
# ill use enumerate to find out the index number of all the even values by using for loop
for index, value in enumerate(a):
    if value % 2 == 0:
        even_indices.append(index)
# Sort the array
sorted_array = np.sort(a)

# Slice elements from index 3 to the end of the array
slice_1 = a[3:]

# Slice elements from index 0 to index 4
slice_2 = a[:5]

# Print [32, 15, 67] using negative slicing
negative_slice = a[-5:-2]

# Print the answers
print("Indices of even numbers:", even_indices)
print("Sorted array:", sorted_array)
print("Slice from index 3 to the end:", slice_1)
print("Slice from index 0 to index 4:", slice_2)
print("Negative slice [32, 15, 67]:", negative_slice)