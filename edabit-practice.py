# Return the sum of two numbers
def addition(a, b):
    return a + b


print("3 + 5 =", addition(3, 2))


# Return hello message in hello() function
def hello():
    return "hi roger"


print(hello())


# return area of triangle
def tri_area(base, height):
    area = (base * height) / 2

    return area


print(tri_area(3, 2))


# to_int() : A function to convert a string to an integer.
# to_str() : A function to convert an integer to a string.

def to_int(txt):
    return int(txt)


print(to_int('123'))


def to_str(num):
    return str(num)


print(to_str(123))
