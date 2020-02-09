#  make a list of five usernames, including admin. print hello and special message for admin

usernames = ['roger', 'katie', 'riley', 'admin', 'asher']
# usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username.title()}")
            print("Would you like to see a status report?")
        else:
            print(f"hello {username.title()}")
else:
    print("There are no users")

#  create new list and check if username already exists
new_users = ['adam', 'elizabeth', 'west', 'Asher']
for new_user in new_users:
    if new_user.lower() in usernames:
        print(f"{new_user.title()} is taken")
    else:
        print(f"{new_user.title()} is available")






