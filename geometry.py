def geometry(shape):
    if len(shape) == 3:
        a = shape[0]
        b = shape[1]
        c = shape[2]

        if (a+b) > c and (a+c) > b and (b+c) > a:
            if (a == b) and (a == c) and (b == c):
                print("This is equilateral triangle.")
            elif (a == b) or (a == c) or (b == c):
                print("Isosceles triangle")
            elif (a == 3) and (b == 4) and (c == 5):
                print("Special right triangle")
            elif (a == 5) and (b == 12) and (c == 13):
                print("Special right triangle")
            elif (a == 8) and (b == 15) and (c == 17):
                print("Special right triangle")
            elif (a == 7) and (b == 24) and (c == 25):
                print("Special right triangle")
            else:
                print("Scalene triangle")

        else:
            print("This is not a triangle")

    elif len(shape) == 4:
        a = shape[0]
        b = shape[1]
        c = shape[2]
        d = shape[3]

        if (a == b) and (a == c) and (a == d):
            print("Square")
        elif (a == c) and (b == d):
            print("Rectangle")
        else:
            print("Quadrilateral")

    elif len(shape) == 5:
        a = shape[0]
        b = shape[1]
        c = shape[2]
        d = shape[3]
        e = shape[4]

        if (a == b) and (a == c) and (a == d) and (a == e):
            print("Regular pentagon")
            print("One interior angle :",oneinteriorangle)
            print("One exterior angle :",exterioranglesum)
            print("Sum of interior angles :",interioranglesum)
            print("Sum of exterior angles :",exterioranglesum)
        else:
            print("Pentagon")

    elif len(shape) == 6:
        a = shape[0]
        b = shape[1]
        c = shape[2]
        d = shape[3]
        e = shape[4]
        f = shape[5]

        if (a == b) and (a == c) and (a == d) and (a == e and (a == f)):
            print("Regular hexagon")
            print("One interior angle :",oneinteriorangle)
            print("One exterior angle :",exterioranglesum)
            print("Sum of interior angles :",interioranglesum)
            print("Sum of exterior angles :",exterioranglesum)
        else:
            print("Hexagon")

    else:
        print("Shape not calculated")

while (True):

    sides = int(input("Enter the length of the sides: "))
    oneinteriorangle = (sides - 2)*180/(sides)
    interioranglesum = (sides - 2)*180
    oneexteriorangle = 360/(sides)
    exterioranglesum = 360

    if (sides == 3):
        a = int(input("opposite: "))
        b = int(input("adjacent: "))
        c = int(input("hypotenuse: "))
        geometry([a,b,c])

    elif (sides == 4):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        d = int(input("d: "))
        geometry([a,b,c,d])

    elif (sides == 5):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        d = int(input("d: "))
        e = int(input("e: "))
        geometry([a,b,c,d,e])

    elif (sides == 6):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        d = int(input("d: "))
        e = int(input("e: "))
        f = int(input("f: "))
        geometry([a,b,c,d,e,f])

    else:
        print("Shape not calculated")
