#making a function with one default value
def student(std_name,std_id,course="BSU CC"):
    #printing a message in dictionary
    student_info={"Name:":std_name,"ID:":std_id,"Course:":course}
    print(student_info)
#calling function by putting the first 2 value    
student(std_name="alpha",std_id=2022122)
#calling the function and also changing the default value
student(std_name="john",std_id=205722,course="BSU BM")