# Write a program that calculates the number of seconds in a day.
# Hint: Ask user to enter number of days, Convert days into hours, hours to minutes, minutes to seconds



#asking user the number of days
days=int(input("Enter number of days you want to convert: "))

#there are 24 hours in one day so we multiply the number of days with 24
hours=24*days

#60 minutes in one hour
minutes=60*hours

#60 seconds in one minute
seconds=60*minutes

#message to be displayed if user enters 0
if days==0:
    print("Sorry,anything multiplied by zero is zero\ntry typing a different number")
#the reason i have a seperate message for user typing 1 day is to avoid the code from printing 1 days as plural
#and to print 1 "day" instead of "days"
elif days==1:
    print("There are 24 hours 1440 minutes and 86400 seconds in a single day")
#in case user types a negative number
#it can still give the accurate answer in the default else statement but just in case it is -1
#there won't be a grammar mistake in printing the answer
elif days==-1:
    print("There are -24 hours -1440 minutes and -86400 seconds in -1 day")
#this is the default answer if user types anything other than 0, 1 or -1
else:
    print("There are",hours,"hours",minutes,"minutes and",seconds,"seconds in",days,"days")