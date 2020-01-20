
first_name = "roger"
last_name = "mayer"

# format strings

full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")


# adding whitespace

print("python")
print("\tPython")  # adds tab to printed line
print("Languages: \nPython\nCSS\nJavaScript")  # new line

print("Languages: \n\tPython\n\tCSS\n\tJavaScript") # new line

# removing whitespace

extra_space = "hello   "
print(extra_space, "|")
extra_space = extra_space.rstrip()
print(extra_space, "|")

