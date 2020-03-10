#  write a loop that prompts user to enter a list of pizza topppings.
#  as they enter each topping, print a message saying you'll add topping.
#  enter quit to exit

prompt = "\n Please enter topping for your pizza:"
prompt += "\n Enter 'quit' when finished \n"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"you've added {topping} to your pizza")
