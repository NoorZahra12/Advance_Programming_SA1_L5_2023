count=1
#as long as the count variable is smaller or equal to 10 the loop will keep looping
while count<=10:
    #if the remainder of the number divided by 2 is 0
    #it means it is an even number
    if count%2==0:
        #printing the even number and increasing it by 1
        print(count)
        count+=1
    else:
        #if the number is odd it will simply increment by 1 without printing the odd number
        count+=1