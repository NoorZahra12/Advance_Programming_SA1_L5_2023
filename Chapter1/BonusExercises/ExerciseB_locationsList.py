# Using the list 
# locations =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']

# - Print the list and find the length of the list☑️
# - Use sorted() to print your list in alphabetical order without modifying the actual list.☑️
# - Show that your list is still in its original order by printing it.☑️
# - Use sorted() to print your list in reverse alphabetical order without changing the order of the original list☑️
# - Show that your list is still in its original order by printing it again.☑️
# - Use reverse() to change the order of your list.☑️
# - Print the list to show that its order has changed.☑️
# - Use sort() to change your list so it’s stored in alphabetical order.☑️
# - Print the list to show that its order has been changed.☑️
# - Use sort() to change your list so it’s stored in reverse alphabetical order.☑️
# - Print the list to show that its order has changed.☑️




locations =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']

# - Print the list and find the length of the list
list_length=len(locations)
print("The length of list is: ",list_length)

# - Use sorted() to print your list in alphabetical order without modifying the actual list.
aplhabetic_order=locations.sort()
print("\nAlphabetical order: ",aplhabetic_order)

# - Show that your list is still in its original order by printing it.
print("Original Order: ",locations)

# - Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
reversed_alphabeticOrder=sorted(locations, reverse=True)
print("\nReversed alphabetical order: ",reversed_alphabeticOrder)
# - Show that your list is still in its original order by printing it again.
print("Original Order: ",locations)

# - Use reverse() to change the order of your list.
locations.reverse()
# - Print the list to show that its order has changed.
print("\nUsing reverse() method and printing the list:",locations)

# - Use sort() to change your list so it’s stored in alphabetical order.
locations.sort()
# - Print the list to show that its order has been changed.
print("Using sort() and printing the list",locations)

# - Use sort() to change your list so it’s stored in reverse alphabetical order.
locations.sort(reverse=True)
# - Print the list to show that its order has changed.
print("changing the list in reverse using sort(): ",locations)