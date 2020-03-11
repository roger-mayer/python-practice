responses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for users name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb: ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else would like to take the poll
    repeat = input('Would another person like to answer? y/n: ')
    if repeat == 'n':
        polling_active = False

# Polling is complete. Show results
print("\n --POLL RESULTS--")
for name, response in responses.items():
    print(f"{name} would like to go to {response}.")