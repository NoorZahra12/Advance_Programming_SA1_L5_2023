#Create a dictionary that contains relevant data for films 
# (e.g. Title, Director, etc). Display the film details using loop

#making a dictionary for avengers
my_film_dictionary={
    'film':'avenger',
    'directer':'Joseph Vincent Russo',
    'year':'2012'
}

#using for loop to display the dictionaries in a neat way
#using .items() method to print both the key and value inside dictionary
for key, values in my_film_dictionary.items():
  #using .title() method to capitalize the first letters
  print(key.title(),": ",values.title())