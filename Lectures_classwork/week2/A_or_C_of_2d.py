#trianlge,circle,rectangle,square

shape=input("trianlge, circle, rectangle or square:  ")

#TRIANGLE
if shape == "triangle":
    option=input("type 'a' for area or 'c' for circumference: ")

    #AREA
    if option == "a":
        b=int(input("enter breadth: "))
        h=int(input("enter height: "))
        #formula
        triangleA=(b*h)/2
        print("\nArea of triangle is: ",triangleA)

    #CIRCUMFERENCE
    elif option == "c":
        a=int(input("enter number of the 1st angle: "))
        b=int(input("enter number of the 1st angle: "))
        c=int(input("enter number of the 1st angle: "))
        #formula
        triangleC=a+b+c
        print("\nCircumference of triangle is: ",triangleC)

    #NONE
    else:
        print("sorry it is not available")


#CIRCLE
elif shape == "circle":
    option=input("type 'a' for area or 'c' for circumference: ")

    #AREA
    if option == "a":
        r=int(input("enter radius: "))
        #formula
        circleA=3.14*r**2
        print("\nArea of circle is: ",circleA)

    #CIRCUMFERENCE
    elif option == "c":
        r=int(input("enter radius: "))
        #formula
        circleC=3.14*r*2
        print("\nCircumference of circle is: ",circleC)

    #NONE
    else:
        print("sorry it is not available")


#RECTANGLE
elif shape == "rectangle":
    option=input("type 'a' for area or 'c' for circumference: ")

    #AREA
    if option == "a":
        l=int(input("enter length: "))
        w=int(input("enter width: "))
        #formula
        rectangleA=l*w
        print("\nArea of rectangle is: ",rectangleA)

    #CIRCUMFERENCE
    elif option == "c":
        l=int(input("enter length: "))
        w=int(input("enter width: "))
        #formula
        rectangleC=(2*l)+(2*w)
        print("\Circumference of rectangle is: ",rectangleC)

    #NONE
    else:
        print("sorry it is not available")

#SQUARE
elif shape == "square":
    option=input("type 'a' for area or 'c' for circumference: ")

    #AREA
    if option == "a":
        side=int(input("Enter the length of one side: "))
        #formula
        squareA=side*side
        print("\nArea of rectangle is: ",squareA)

    #CIRCUMFERENCE
    elif option == "c":
        side=int(input("Enter the length of one side: "))
        #formula
        squareC=4*side
        print("\Circumference of rectangle is: ",squareC)

    #NONE
    else:
        print("sorry it is not available")

#in case user wrote a shhape other than trianlge,circle,rectangle, or square
else:
     print("sorry, the shape you entered is not here")