# Your teacher needs help computing the grades for the class and
# you offered to help.  You will use the Python language to help
# compute information to help, but first you need a quick tutorial
# on how to use Python!

# First, the lines that begin with a # are comments.  They allow you
# to comment about what is happening in the program and are ignored
# by Python.

# Python allows you to "name" information.  This "name" is called
# a variable.  The same "name" may contain different information
# while a program runs (executes), but only one piece of
# information can have that name at any one time. When we name
# a piece of information, we say we "assigned" that information
# to a variable.  Here we assign your name to a variable called
# my_name.  Change the information (value) that we assign to 
# my_name to be your name.
my_name = 'Jim'

# You can print the information stored in a variable by using the
# `print` function. Functions sometimes require you to give it
# information.  The information you give a function are called
# _parameters_ and are separated by commas.  The print function
# can take zero or more parameters and will print them on the same
# line with a space between them. (Using (calling) print with no
# parameters will cause an empty line to be printed.)
print("I am a program written by", my_name)

# After your program says 'I am a program written by <your name>', remove
# this next line. exit() is a function that stops the program.
exit()

# In life you often need to make decisions and those decisions have
# consequences. For instance, 
#   If I do my chores, then it'll get my allowance. 
# The same is true when you're programming. You often make
# choices about what should happen using `if`s.  Often times there things
# happen when you do something and when you don't.  For instance,
#   If I do my chores, then I'll get my allowance, otherwise I can't play games
# In programming `else` is used in place of otherwise.

chores_are_done = True
if chores_are_done:
    print("I get allowance")
else:
    print("I can't play games")

# Like in real life, things can be True or False. It is False that the sky 
# is purple.  Pretend that it's False that you did your chores and run the 
# program again. Instead of getting an allowance, the program will tell you # that you can't play games. Once you can get the program to say what # happens when you do or don't do your chores, delete the next line.
exit()

# Notice that in the above the print functions have spaces before them.
# These spaces have a special meaning; they are called indentation. You can 
# use any number of spaces that you want, but you must use the same number
# all the time.  Most people use 4, and all the programs in this book will
# also use 4 spaces.

# Things that are indented are called 'blocks'.  The 'if-block' above is
# if statement, and the print statement.  The 'else-block' above is the 
# else statement and the print statement below it. Blocks often have more 
# than a single statement

chores_are_done = True
my_money = 0.0
if chores_are_done:
    print("I get allowance")
    my_money += 5.0
else:
    print("I can't play games")

# Here the 'if-block' is the if statement, the print function, and the 
# addition statement.

exit()

# We'll come back to blocks, but first, let's talk about lists. Lists, just 
# a grocery list, is a sequence of things. Unlike when you read a list in
# English, you don't put an and before the last thing (item) in Python.
# Like writing a list in English, you put commas between items in Python.
# Unlike in English, when you write a list in Python you put square 
# brackets [] around it.

grocery_list = ['Milk', 'Eggs', 'Yoghurt', 'Apples', 'Oranges', 'Bread']

# We often need to do things with each item in the list.  For each item in 
# a list, we want to do the same thing. Like a loop on a roller coaster, 
# where you start at the bottom, go to the top, and then come back to the
# bottom, we 'loop' in the code by starting at the top, executing to the 
# bottom of the block, and then going back to the top.

for grocery in grocery_list:
    print('Picking up', grocery)

# This is called a 'for-loop'.  It goes through the list one item at a time
# and stores it in the variable grocery. The 'for-block' is the for 
# statement and the print statement.

exit()

# Blocks can have blocks inside them, for instance

for grocery in grocery_list:
    print('Picking up', grocery)
    if grocery == 'Apples':
        print('Yum!')

# The 'for-block' is now a for statement, a print function, and an if-block.

exit()

# Sometimes we need to keep track of a information by names that we don't
# know when writing the program, or would otherwise need a lot of variables.
# To keep track of the grocery list and what we have and haven't picked up
# We could have a variable for each item.
picked_up_Milk = False
picked_up_Eggs = False
picked_up_Yoghurt = False
picked_up_Apples = False
picked_up_Oranges = False
picked_up_Bread = False

for grocery in grocery_list:
    print('Picking up', grocery)
    
    if grocery == 'Apples':
        print('Yum!')
        picked_up_Apples = True
    elif grocery == 'Milk':
        picked_up_Milk = True
    elif grocery == 'Eggs':
        picked_up_Eggs = True
    elif grocery == 'Yoghurt':
        picked_up_Yoghurt = True
    elif grocery == 'Oranges':
        picked_up_Oranges = True
    elif grocery == 'Bread':
        picked_up_Bread = True

# If we add cheese to our list, we have to edit the program
# to account for cheese.  This is both tedious and error-prone.
# To avoid doing this, Python has something called a Dictionary.
# Like a dictionary where you can look up words and their definitions,
# Python dictionaries let you look something up, to get something else.

words = { 'Python': '1. A breed of snake. 2. A great programming language'}

# To look something up, we can add square brackets to the end of the 
# variable and put inside what we want to look up
print(words['Python'])

exit()

# An empty dictionary is created with two curly braces with nothing in 
# between

picked_up = {}

# We now have a dictionary named picked_up and can use it to rewrite the 
# grocery program above

for grocery in grocery_list:
    print("Picking up", grocery)
    picked_up[grocery] = True

print(picked_up)

exit()
