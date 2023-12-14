# Write a program to display the following pattern using nested loops.

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num=5
#the first loop is the number of rows which is 5 rows in total but since wriing 5 will print 4 rows
#i am writing num+1 so it makes it 6 and it will display 5 rows
for row in range(1,num+1):
    #this nested loop is for the columns inside the row
    #the columns will increase by 1 in each row
    for column in range(1,row+1):
        #print i want the columns to display in the same row so im changing the print's default ending with a space instead of \n
        print(column,end=' ')
    # printing empty rows because print by default ends with \n
    # so i dont need to type print("\n") to display a new row n leave it empty
    print()