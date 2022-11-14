import math


def processMenu():
    print('Geometry Calculator')
    print('-------------------')
    print('<1> Area of a Circle')
    print('<2> Circumference of a Circle')
    print('<3> Area inside of a Sphere (volume)')
    print('<4> Area of a Rectangle')
    print('<5> Perimeter of a Rectangle')
    print('<6> Area of a Square')
    print('<7> Perimeter of a Square')
    print('<8> Area inside of a Cube (volume)')
    print('<999> End the program\n')

    user_input = input('Please select an option: ')

    while user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4' and user_input != '5' and user_input != '6' and user_input != '7' and user_input != '8' and user_input != '999':
        if not user_input.isnumeric():
            print('** Error: Your input must be numeric, try again\n')
        else:
            print('** Error: Invalid Menu selection\n')

        print('Geometry Calculator')
        print('-------------------')
        print('<1> Area of a Circle')
        print('<2> Circumference of a Circle')
        print('<3> Area inside of a Sphere (volume)')
        print('<4> Area of a Rectangle')
        print('<5> Perimeter of a Rectangle')
        print('<6> Area of a Square')
        print('<7> Perimeter of a Square')
        print('<8> Area inside of a Cube (volume)')
        print('<999> End the program\n')

        user_input = input('Please select an option: ')

    return user_input


# <1> Area of a Circle
def circleArea(radius):
    area = math.pi * math.pow(radius, 2)
    return format(area, '.4f')


# <2> Circumference of a Circle
def circleCircumference(radius):
    circumference = 2 * math.pi * radius
    return format(circumference, '.4f')


# <3> Area inside of a Sphere (volume)
def sphereVolume(radius):
    volume = 4 / 3 * math.pi * math.pow(radius, 3)
    return format(volume, '.4f')


# <4> Area of a Rectangle
def rectangleArea(height, width):
    area = width * height
    return format(area, '.4f')


# <5> Perimeter of a Rectangle
def rectanglePerim(height, width):
    perim = (2 * width) + (2 * height)
    return format(perim, '.4f')


# <6> Area of a Square
def squareArea(side):
    area = math.pow(side, 2)
    return format(area, '.4f')


# <7> Perimeter of a Square
def squarePerim(side):
    perim = side * 4
    return format(perim, '.4f')


# <8> Area inside of a Cube (volume)
def cubeVolume(side):
    area = math.pow(side, 3)
    return format(area, '.4f')


def main():
    user_input = processMenu()
    while user_input != '999':
        # <1> Area of a Circle
        if user_input == '1':
            radius = float(input('What is the radius of the circle? '))
            area = circleArea(radius)
            print('Answer: Area of the circle is  ', area)

        # <2> Circumference of a Circle
        elif user_input == '2':
            radius = float(input('What is the radius of the circle? '))
            circumference = circleCircumference(radius)
            print('Answer: Circumference of the circle is  ', circumference)

        # <3> Area inside of a Sphere (volume)
        elif user_input == '3':
            radius = float(input('What is the radius of the sphere? '))
            volume = sphereVolume(radius)
            print('Answer: Volume of the sphere is  ', volume)

        # <4> Area of a Rectangle
        elif user_input == '4':
            height = float(input('What is the height of the rectangle? '))
            width = float(input('What is the width of the rectangle? '))
            area = rectangleArea(height, width)
            print('Answer: Area of the rectangle is  ', area)

        # <5> Perimeter of a Rectangle
        elif user_input == '5':
            height = float(input('What is the height of the rectangle? '))
            width = float(input('What is the width of the rectangle? '))
            perim = rectanglePerim(height, width)
            print('Answer: Perimeter of the rectangle is  ', perim)

        # <6> Area of a Square
        elif user_input == '6':
            side = float(input('What is the side length of the square? '))
            area = squareArea(side)
            print('Answer: Area of the square is  ', area)

        # <7> Perimeter of a Square
        elif user_input == '7':
            side = float(input('What is the side length of the square? '))
            perim = squarePerim(side)
            print('Answer: Perimeter of the square is  ', perim)

        # <8> Area inside of a Cube (volume)
        elif user_input == '8':
            side = float(input('What is the side length of the cube? '))
            volume = cubeVolume(side)
            print('Answer: Volume of the cube is  ', volume)

        print('\n')
        user_input = processMenu()

    print('Program ending, have a nice day')


if __name__ == '__main__':
    main()
