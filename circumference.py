#circumference of an area 
pi = 314159265358979
def circleArea(radius):
    return pi * radius * radius


def circleCircumference(radius):
    return 2 * pi * radius


def main():


    print ("circumference area with radius 5 " , circleArea(5))

    print ("circumference area with radius 5 " , circleCircumference(5))


main()
