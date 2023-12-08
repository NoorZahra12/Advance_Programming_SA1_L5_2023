
# taking user input
num = int(input("Enter a number: "))
# using end so it will be in the same line and wont display \n
print(num, "=", end=" ")
# after displaying num = now in each column of the samee row i will just reduce the num until it hits 1
for column in range(1, num + 1):
    # using end to make sure they dont print in new line
    print(num, 'x ', end="")
    num -= 1
    # until here it will display 4 = 4 x 3 x 2 x 1 x  

    # the number will reduce itself by 1, but when it reaches 1 print 1 only and break the for loop
    # to avoid the 3 = 3 x 2 x 1 x
    # if it reaches 1, print 1 only and this is the end of the loop
    if num == 1:
        print("1") 
        break

