# Given the names and grades for each student in a Physics class of
# students, store them in a nested list and print the name(s) of any student(s)
# having the second lowest grade.

# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry,
# so we order their names alphabetically and print each name on a new line.


marksheet = []
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet += [[name, score]]
        scorelist += [score]
    b = sorted(list(set(scorelist)))[1]

    for a, c in sorted(marksheet):
        if c == b:
            print(a)

