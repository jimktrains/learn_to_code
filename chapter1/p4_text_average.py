# Your teacher now wants to know the average grade on each test

import csv

with open('grades.csv') as grades_file:
    grades = csv.DictReader(grades_file)
    # Instead of using a single variable to store the total and count
    # We will use two dictionaries to store the count and total for
    # each test
    test_count = {}
    test_total = {}
    for student_tests in grades:
        for test in student_tests:
            if test != 'Student':
                # We need to initialize the count and total with
                # 0 before we can use it.  To do this we need to check
                # if we've seen this test before.
                if test not in test_count:
                    test_count[test] = 0
                if test not in test_total:
                    test_total[test] = 0
                test_count[test] += 1
                test_total[test] += int(student_tests[test])

# After we have the counts and totals for each test, we can loop
# over the tests and compute and then print the average for each
for test in test_count:
    print(test, test_total[test] / test_count[test])
