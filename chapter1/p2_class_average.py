# The average of a series of numbers is the total sum of all
# the numbers divided by the count of the numbers.
# The average of 1,1,2,4,7 is (1+1+2+4+7)/5 = 15/5 = 3
# This program will find the average score of the class 
# for all 4 exams
import csv

# When we opened a file in P1, we assigned it
# to a variable and had to close it when we were done.
# Python offers a way to make sure a file gets closed
# (even if there is an error in the program), without
# you having to close it yourself. This is called a
# with-block.  It assigns the file we open to grades_file
# and at the end of the block, automatically closes it
# for us
with open('grades.csv') as grades_file:
    grades = csv.DictReader(grades_file)
    # Computing an average requires knowing 2 things:
    # * total sum of all the numbers
    # * count of numbers
    # We will store each of these values in a variable
    test_count = 0
    test_total = 0
    
    for student_tests in grades:
        # When we printed student_tests in P1, we saw that
        # it contained the student's name and test scores.
        # Since we only want the test scores, we can loop
        # over the test scores and the name, and only
        # add test scores, skipping over the student's name
        for test in student_tests:
            if test != "Student":
                # Each time we see a test, we do two things:
                # * Increment the count of tests by one
                # * Add the test score to the total of all the tests
                test_count += 1
                test_total += int(student_tests[test])

# To get the average, all we need to do
# is divide the total of all the scores
# by the count of the scores.
# We then store the average in a variable.
test_average = test_total/test_count

# We can print this average by using the print function.
print(test_average)
