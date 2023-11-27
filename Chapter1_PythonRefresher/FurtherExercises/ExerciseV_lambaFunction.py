# Create the list marks with the given values
# marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]
# Using lambda function in the function sort the list elements of the tuple based on marks low to high and high to low


marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]
#printing the original marks
print("Original Order:")
#printing the list using for loop
for course, mark in marks:
    print(" ",course, mark) #adding space in the start of each line to make the output look neat

################ Ascending Order ######################
# sorting the tuples inside marks list by using sorted()
# key is a parameter and im using lamba function to select the second element in each tuple
# writing 1 to get the second element as numbers start from 0 so the second element's index is 1
ascending_order = sorted(marks, key=lambda x: x[1])

print("\nAscending Order:")
for course, mark in ascending_order:
    print(" ",course, mark)

################ Descending Order #####################
#doing the same thing i did in ascending order but adding reverse true to reverse the order
descending_order = sorted(marks, key=lambda x: x[1] , reverse=True)

print("\n\nDescending Order:")
for course, mark in descending_order:
    print(" ",course, mark)