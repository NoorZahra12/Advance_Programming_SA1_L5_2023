# Create a tuple with values
# year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)
# - Access the value at index -3
# - Reverse the tuple and print the original tuple and reversed tuple 
# - Count number of times 2009 is in the tuple (use count() method) 
# - Get the index value of 2018(Use index method) 
# - Find length of given tuple(Use len() method)


year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)
print(year,"\n3rd index:",year[2],"\t-3rd index: ",year[-3])
#reversing tuple
reverse= tuple(reversed(year))
print("\nOriginal year list:",year,"\nReversed year list: ",reverse)

#counting how many times 2009 appeared in the tuple
counting_2009=year.count(2009)
print("\nThe amount of times 2009 is repeated: ", counting_2009)

#finding the index of 2018 in tuple
index_of_2018=year.index(2018)
print("The index number of 2018 is: ", index_of_2018)

#finding the total length in tuple
total_length=len(year)
print("The total elements inside list is : ",total_length)