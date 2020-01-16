# comment
print("hello world")

x = 5
y = "John"
print(x)
print(y)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = "Python is "
y = "awesome"
z = x + y
print(z)

"""If you create a variable with the same name inside
a function, this variable will be local,
and can only be used inside the function.
The global variable with the same name will remain as it was,
global and with the original value."""
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)
"""There are three numeric types in Python:
int
float
complex
Variables of numeric types are created when you assign a value to them:
Example"""
x = 1  # int
y = 2.8  # float
z = 1j  # complex
"""To verify the type of any object in Python, use the type() function:
Example"""
print(type(x))
print(type(y))
print(type(z))

for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

hi = "hello"
print(hi)
