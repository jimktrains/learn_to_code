# The grades are stored in a comma-separated-value (CSV) file.
# This means that each student (record) is on its own line and
# the student name and grades (fields) have commas between them.
# Python has a build in set of code (module) that we can use
# (import) into our program to make it easy to use CSV files.
import csv

# Here we assign the name of the file to the variable
# file_name.
file_name = 'grades.csv'

print("The file I'm going to read is called", file_name)

# To read the file stored in file_name, we use an `open` function.
# The open function takes two parameters:
#  * The name of the file to open (we stored this in file_name)
#  * How we want to open the file (are we getting information from it
#    (reading) or putting information in it (writing).  We just want to
#    read the information, so we use a 'r' for the second parameter
grades_file = open(file_name, 'r')

# Since we know grades_file is in CSV format, we can make use of a
# premade function to help us get information from it. The DictReader
# (short for Dictionary Reader) in the csv module (that we imported
# earlier) will read the CSV file and return a list of Dictionaries
grades = csv.DictReader(grades_file)

# To print out each student's name and scores all we need to do
# is loop over the grades to get each students and then call the
# print function.
for student_grades in grades:
    print(student_grades)

# When you open a door, you need to close it after you.  Like a door,
# files need to be closed when you're finished with them. If you don't
# close the file, the computer may think you still have it open and not
# let you open it again.
grades_file.close()
