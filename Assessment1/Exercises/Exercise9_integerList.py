# Create an integer list and perform following operations
# - Create an int list with 10 values
# - Output the list using a for loop
# - Output the highest and lowest value
# - Sort the elements in ascending order
# - Sort the elements in descending order
# - Append two elements 
# - Print the list after appending


my_num_list=[3,10,5,7,6,1,8,2,9,4]
print("My list: ")
for i in my_num_list:
    print(i,end=" ")

highest_element=max(my_num_list)
lowest_element=min(my_num_list)

print("\n\nHighest number: ",highest_element,"\nLowest number is: ",lowest_element)
my_num_list.sort()
print("\nAscending order list: ",my_num_list)
my_num_list.reverse()
print("Descending order list: ",my_num_list)
#adding two elements at the end of the list by using append
my_num_list.append(11)
my_num_list.append(12)
print("\nNew list: ",my_num_list)