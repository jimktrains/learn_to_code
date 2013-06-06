import csv

with open('grades.csv') as grades_file:
    grades = csv.DictReader(grades_file)
    student_test_count = {}
    student_test_total = {}
    for student_tests in grades:
        student_name = student_tests['Student']
        student_test_count[student_name] = 0
        student_test_total[student_name] = 0
        for test in student_tests:
            if test != 'Student':
                student_test_count[student_name] += 1
                student_test_total[student_name] += int(student_tests[test])
for student_name in student_test_count:
    print(student_name, student_test_total[student_name] / student_test_count[student_name])
