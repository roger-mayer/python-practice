# removing all instances of specific value from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

for pet in pets:
    print(pet)

if 'cat' in pets:
    while 'cat' in pets:
        pets.remove('cat')

    pets.append('cats')

print(pets)
