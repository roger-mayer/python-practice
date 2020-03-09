# using continue in a loop

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
        # this will skip even numbers

    print(current_number)
