'''
Author: Paolo Pedrigal
Date: 10/18/2021
Description: CLI for calulcating GPA in the 4.0 scale
'''
from collections import defaultdict

# TODO:
# - add generator function?
# - make cap insensitive
# - make restrictions on user entries (e.g. user cant enter a letter instead of a number for the units)
# - generate a dataframe for the data and convert them into an excel sheet

# Declare variables
grade_converter = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0}


# Ask user for list of classes
print("Please enter your courses:")
print("Format: course units grade")
print("---------------------------")
grades = defaultdict(float)

course_grade = input("\n")


while course_grade != "-end" and course_grade != "-END":

    if course_grade == "-undo" or course_grade == "-UNDO":   # Undo action
        if not grades: # empty dictionary
            pass
        else: # pops last dicionary item
            grades.pop(list(grades.keys())[-1])

    elif len(course_grade.split()) != 3: # user enters an invalid entry
        pass

    else: # general
        grades[course_grade.split()[0]] = (float(course_grade.split()[1]), float(course_grade.split()[2])) # CHANGE THIS LATER
    course_grade = input("\n")

# Print classes for user reference
for course, units_grades in grades.items():
    print(course + ":", units_grades[0], "units,", units_grades[1])

# Ask user for confirmation for grade entries

# Edit course grade if user wants to change a grade

# Calculate GPA
numerator = sum(list(map(lambda x: x[0]*x[1], grades.values())))
denominator = sum(list(map(lambda x: x[0], grades.values())))
print(numerator)
print(denominator)
gpa = numerator / denominator
print("---------")
print("GPA:", gpa)