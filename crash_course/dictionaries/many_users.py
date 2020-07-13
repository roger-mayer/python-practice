#  dictionary in a dictionary
users = {
    'rmayer': {
        'first': 'roger',
        'last': 'mayer',
        'age': 35
    },
    'kwest': {
        'first': 'katie',
        'last': 'west',
        'age': 28
    },
    'amayer': {
        'first': 'asher',
        'last': 'mayer',
        'age': 1
    }

}

for username, user_info in users.items():
    print(f"\nusername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    user_age = user_info['age']

    print(f"Full Name: {full_name.title}")
    print(f"Age: {user_age}")


