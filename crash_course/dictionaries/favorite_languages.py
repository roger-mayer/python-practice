favorite_languages = {
    'roger': ['python', 'react'],
    'asher': ['java'],
    'riley': ['javascript', 'ruby'],
    'katie': ['love', 'basketball'],
}

for name, languages in favorite_languages.items():
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
