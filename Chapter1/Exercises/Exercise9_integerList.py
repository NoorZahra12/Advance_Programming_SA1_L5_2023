# Create an integer list and perform following operations
# - Create an int list with 10 values
# - Output the list using a for loop
# - Output the highest and lowest value
# - Sort the elements in ascending order
# - Sort the elements in descending order
# - Append two elements 
# - Print the list after appending


my_num_list=[3,10,5,7,6,1,8,2,9,4]
#printing list in for loop
print("My list: ")
for i in my_num_list:
    print(i,end=" ") #using end to make it display in one line with a space instead of new line

highest_element=max(my_num_list) #finding the highest element using max()
lowest_element=min(my_num_list) #finding the smallest element using max()
print("\n\nHighest number: ",highest_element,"\nLowest number is: ",lowest_element)

#sorting it from lowest to highest with sort()
my_num_list.sort()
print("\nAscending order list: ",my_num_list)

#reversing the sorted list to display it from highest to loswest with reverse()
my_num_list.reverse()
print("Descending order list: ",my_num_list)

#adding two elements at the end of the list by using append
# it will append at the end of the list
my_num_list.append(11)
my_num_list.append(12)
print("\nNew list: ",my_num_list)