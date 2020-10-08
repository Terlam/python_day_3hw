from math import pi
def sqft():
    a = input('house length: ')
    b = input('house width: ')
    num = int(a) * int(b)
    print(f'{num}sqft')


def circum():
    radius = int(input("Give me the radius of your circle: "))
    circ = int(radius) *  2 * pi
    print(f'the circumfrence is {circ}')

