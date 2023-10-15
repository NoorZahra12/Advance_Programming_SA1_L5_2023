#making a function which will display the name of a film with a message
def fav_film(film_name):
    #displaying message and also capitalizing the first letters of every word by using .title()
    print("Your favorite movie is:", film_name.title())

#calling the function and
#taking input from user for the film_name value
fav_film(input("what is your favorite film? "))