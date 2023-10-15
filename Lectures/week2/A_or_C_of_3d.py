shape=input("sphere, cube, cuboid or pyramid: ")

#SPHERE
if shape == "sphere":
    option=input("type 'a' for area or 'v' for volume: ")

    #AREA
    if option == "a":
        r=int(input("enter a radius: "))
        #formula
        sphereA=4*3.14**r*2
        print("\nArea of sphere is: ",sphereA)

    #VOLUME
    elif option == "v":
        r=int(input("enter a radius: "))
        #formula
        sphereV= 3.14*(r**3)*(4/3)
        print("\nVolume of sphere is: ",sphereV)

    #NONE
    else:
        print("sorry it is not available")


#CUBE
elif shape == "cube":
    option=input("type 'a' for area or 'v' for volume: ")

    #AREA
    if option == "a":
        s=int(input("enter length of one side: "))
        #formula
        cubeA=6*(s**2)
        print("\nArea of cube is: ",cubeA)

    #VOLUME
    elif option == "v":
        s=int(input("enter length of one side: "))
        #formula
        cubeV=s**3
        print("\nVolume of cube is: ",cubeV)

    #NONE
    else:
        print("sorry it is not available")

#CUBOID
elif shape == "cuboid":
    option=input("type 'a' for area or 'v' for volume: ")

    #AREA
    if option == "a":
        l=int(input("enter length: "))
        h=int(input("enter height: "))
        b=int(input("enter breadth: "))
        #formula
        cuboidA=2*(l*b+b*h+l*h)
        print("\nArea of cuboid is: ",cuboidA)

    #VOLUME
    elif option == "v":
        l=int(input("enter length: "))
        h=int(input("enter height: "))
        b=int(input("enter breadth: "))
        #formula
        cuboidV=l*h*b
        print("\nVolume of cuboid is: ",cuboidV)

    #NONE
    else:
        print("sorry it is not available")
        
#PYRAMID
elif shape == "pyramid":
    option=input("type 'a' for area or 'v' for volume: ")

    #AREA
    if option == "a":
        p=int(input("enter perimeter: "))
        l=int(input("enter length of height: "))
        b=int(input("enter base: "))        
        #formula
        pyramidA=(1/2)*p*l+b
        print("\nArea of pyramid is: ",pyramidA)

    #VOLUME
    elif option == "v":
        b=int(input("enter base: "))
        h=int(input("enter height: "))
        #formula
        pyramidV=b*h*(1/3)
        print("\nVolume of pyramid is: ",pyramidV)

    #NONE
    else:
        print("sorry it is not available")

#if the user wrote a different shape other than sphere, cube, cuboid or pyramid
else:
     print("sorry the shape you entered is not available")