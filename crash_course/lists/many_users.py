users = {
    'rmayer': {
      'first': 'roger',
      'last': 'mayer',
      'location': 'texas',
        },
    'kwest': {
        'first': 'katie',
        'last': 'west',
        'location': 'utah',
        }
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    fullname = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {fullname.title()}")
    print(f"\tLocation: {location.title()}")


