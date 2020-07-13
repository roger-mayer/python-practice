def describe_pet(pet_name, animal_type='fish'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('sky', 'dog')
describe_pet('waffles', 'cat')
describe_pet('goldie')


