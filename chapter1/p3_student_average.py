# Your teacher now wants to know the average grade of each student

import csv

with open('grades.csv') as grades_file:
    grades = csv.DictReader(grades_file)
    # Instead of using a single variable to store the total and count
    # We will use two dictionaries to store the count and total for
    # each student
    student_test_count = {}
    student_test_total = {}
    for student_tests in grades:
        student_name = student_tests['Student']
        # We need to initialize the count and total with
        # 0 before we can use it
        student_test_count[student_name] = 0
        student_test_total[student_name] = 0
        for test in student_tests:
            if test != 'Student':
                student_test_count[student_name] += 1
                student_test_total[student_name] += int(student_tests[test])

# After we have the counts and totals for each student, we can loop
# over the students and compute and then print the average for each
for student_name in student_test_count:
    print(student_name, student_test_total[student_name] / student_test_count[student_name])

# Your teach now wants both the average and the letter grade.  Modify the 
# program above to print the student's name, average, and letter grade.
