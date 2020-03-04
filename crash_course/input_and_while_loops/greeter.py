# # single line
# name = input("please enter your name: ")
# print(f"Hello, {name}!")
#
# # multi line prompt
# prompt = "If you tell us you name, we can personalize messages."
# prompt += "\nWhat is your name? "
#
# name = input(prompt)
# print(f"\nHello, {name}!")

# using int to accept numerical input
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are an adult")
else:
    print("You are a baby")

# even or odd
num = input("Please enter a number: ")
num = int(num)
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

