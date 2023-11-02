#making a function and naming it sum
def sum(a=10,b=5):
    #using the return statement to send the 
    #result of the function back to the caller
    return a+b

#simply calling a function with it's default values
print("The cylinder volume of default is: ",sum())

#over riding the first default number with 20
answer=sum(20)
print("The cylinder volume of radius=7 is: ",answer)

#changing the default number of both numbers by calling funcion
answer=sum(6,9)
print("The cylinder volume of radius=6 and height=9 is: ",answer)