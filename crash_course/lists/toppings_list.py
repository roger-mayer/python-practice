
requested_toppings = ['mushrooms', 'extra cheese', 'pepperoni']
print("\nIf statement:")
if 'mushrooms' in requested_toppings:
    print(f"adding {requested_toppings[0]}")
if 'extra cheese' in requested_toppings:
    print(f"adding {requested_toppings[1]}")

print("Finished making your pizza")

print("\nFor/if-else list:")
for requested_topping in requested_toppings:
    if requested_topping == 'pepperoni':
        print(f"Sorry we are out of {requested_topping}")
    else:
        print(f"adding {requested_topping} to your pizza")

print("\nUsing multiple lists:")
available_toppings = ['mushrooms', 'pepperoni', 'sausage', 'olives']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping}")
    else:
        print(f"we are out of {requested_topping}")

print("we are finished making your pizza")



