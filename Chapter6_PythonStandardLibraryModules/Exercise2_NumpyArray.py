# For the array a = [20,23,82,40,32,15,67,52] print the output of following
a = [20, 23, 82, 40, 32, 15, 67, 52]


# find the indices of even numbers
evenindices = []
for index, value in enumerate(a):
    if value % 2 == 0:
        evenindices.append(index)

# Sort the array
sortedarray = []
for value in sorted(a):
    sortedarray.append(value)

# Slice elements from index 3 to the end of the array
slice1 = []
for value in a[3:]:
    slice1.append(value)

# Slice elements from index 0 to index 4
slice2 = []
for value in a[:5]:
    slice2.append(value)

# print [32 15 67] using negative slicing
negativeslice = []
for value in a[-5:-2]:
    negativeslice.append(value)

# printing the answers
print("Indices of even numbers:", evenindices)
print("Sorted array:", sortedarray)
print("Slice from index 3 to the end:", slice1)
print("Slice from index 0 to index 4:", slice2)
print("Negative slice [32, 15, 67]:", negativeslice)