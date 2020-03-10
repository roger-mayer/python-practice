#  movie ticket varies by age

prompt = "\nPlease enter your age\n"

age = input(prompt)
age = int(age)

if age < 3:
    print(f"kids age {age} get in free!")
elif age < 12:
    print(f"kids age {age} must pay $10")
else:
    print("you're old and must pay $15")




