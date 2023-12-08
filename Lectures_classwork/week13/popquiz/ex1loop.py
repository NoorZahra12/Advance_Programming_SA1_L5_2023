num=4
#the first loop is the number of rows which is 4 rows in total but since writing 4 will print 3 rows
#i am writing num+1 so it makes it 5 and it will display 4 rows, the reason i am writing 5
# instead of 4 for displaying 5 rows is because it starts from 0 
# so if i want 4 rows starting from 1 i need to type 5 start from 1. therefore (1 , 5) in the range
for row in range(1,num+1):
    #this nested loop is for the columns inside each row
    #the columns will increase by 1 column in each row
    #first row having 1 column, then second row having 2 columns and so on
    for column in range(1,row+1):
        #printing the columns in each row with a space only
        #putting end=' ' with typing nothing inside it. by default the for loop will print in new
        #lines. but i want the columns to be inside one row 
        # so im using end='' to end with a space instead of new line \n
        print(column, end='')
        # now all the columns will display in inline rows


    # printing the rows
    print()