#making a function with one default value
def student(name,id,course="BSU CC"):
    #printing a message
    print("student name is",name,"id:",id,"course:",course)
#calling function by putting the first 2 value    
student(name="alpha",id=2022122)
#calling the function and also changing the default value
student(name="john",id=205722,course="BSU BM")