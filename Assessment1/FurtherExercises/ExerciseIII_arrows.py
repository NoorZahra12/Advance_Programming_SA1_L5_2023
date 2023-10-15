# Write a Python program to print the asterisk pattern shown below
#      *
#     ***
#    *****
#   *******
#  *********
#     ***  
#     ***
#     ***


#first making a pyramid star pattern using for loop for the top part of arrow
#9 columns is the highest
column=9
#ranging from 1 to 9 and printing the 2nd number of column ranging from 1-9 for odd numbers
#i=1,3,5,7,9
for i in range(1,column+1,2):
    #printing space, and the stars with i elements which will increase from 1-9 in odd numbers
    print(" "*(column-1), "*"*i)
    #after printing it, the column is reduced by 1.
    column-=1

#printing the bottom part of the arrow 3 times to display the 3 rows
for j in range(1,4):
    #first printing the space and then the stars
    print(" "*7,"***")