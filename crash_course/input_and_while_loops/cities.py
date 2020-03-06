# using break to exit loop

prompt = "\nPlease enter name of a city you have visited"
prompt += "\nenter 'quit' when you are finished "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to visit {city.title()}!")


