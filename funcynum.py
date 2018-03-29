"""
Ilias Boujlil
3/22/2018
Section 002

funcynum.py (20 points + 3 extra credit)
=====

This file will contain functions that you'll use in feeling_quizzy.py. There
are 4 parts to this file, and they all depend on one another, so they must be 
done in order. The functions in this file will ultimately produce 'ASCII' art 
numbers. For example, the number 5:

*****
*
*****
    *
*****


Part 1 - Create functions that make horizontal and vertical line strings 
-----
Create three functions:

1. horizontal_line(char, width, left_padding)
    * __input__:
        * the character to make the line out of ('*' for example)
        * the total width of the line
        * the number of spaces before the line (left padding)
    * __processing__: 
        * creates a <width> wide string composed of the characters specified, 
          starting with an <left_padding> number of spaces 
    * output: 
        * returns a string representing a horizontal line 

2. vertical_lines(char, height, left_padding, number, interior_offset):
    * input:
        * the character to make the line out of ('*' for example)
        * the total height of the line
        * the number of spaces before the line (left padding)
        * the number of vertical lines to draw
        * the space between each line (an interior offset)
    * processing: 
        * creates a string that represents the specified number of vertical
          lines 
        * each line is <height> tall 
        * and is composed of the characters specified 
        * there are <interior offset> number of spaces between each vertical
          line
        * there is an <left_padding> number of spaces before the lines begin
        * for example, the string, '* *\n* *\n* *\n* *', is a set of two vertical lines, 
          each 4 characters tall, with one space character between the lines, with no left padding. NOTICE THAT THERE IS 
          NO NEW LINE at the end, and there ARE NO TRAILING SPACES
        * YOU MUST USE NESTED LOOPS TO CONSTRUCT THIS STRING
        * hint: the outer loop can represent row, the inner loop can represent
          column... and you can use the col_num or row_num to determine if an
          interior offset or newline should be added
    * output: 
        * returns a string representing a series of vertical lines
        
3. vertical_line(char, height, left_padding):
    * input:
        * the character to make the line out of ('*' for example)
        * the total height of the line
        * the number of spaces before the line (an left padding)
    * processing: 
        * creates a <height> tall string composed of the characters specified, 
          starting with an <left_padding> number of spaces 
        * hint: simply call your vertical_lines function so that only 1 line is
          printed (remember to pass along the left_padding and character, though!)
    * output: 
        * returns a string representing a single vertical line 

Examples:
print(horizontal_line('*', 5, 0))
*****

print(horizontal_line('x', 2, 4))
    xx

print(vertical_line('*', 2, 5))
     *
     *

print(vertical_lines('+', 4, 0, 5, 3))
+   +   +   +   +
+   +   +   +   +
+   +   +   +   +
+   +   +   +   +


Part 2 - Create functions that print out the number 0 - 9, +, and -
-----
Create 12 additional functions that print out the numbers 0 - 9, +, and -. All
numbers will have a flexible width, but you can assume that the HEIGHT OF THE
NUMBERS WILL ALWAYS BE 5. Use the horizontal and vertical line drawing 
functions to write these functions.

The functions will be called print_one, print_two ... print_minus. The general 
input/output/processing chart will looks similar for each functions. Here's an
example input/output/processing chart, an actual function definition for the
function that prints out the number one, and some examples of usage:

print_one(char, width)
* input:  
    * a character to create the number with
    * the width of the number
* processing: 
    * prints an 'ASCII' art number that's 5 characters tall and as wide as the
      argument passed in (<width> characters wide)
    * if a width is less than 3, default to 3
* output:     
    * returns nothing

def print_one(char, width):
    if width < 3:
        width = 3
    print(vertical_line(char, 5, width - 1))

Example Output (note the relationship between the number of leading spaces and
the total width):

print_one('*', 5)
    *
    *
    *
    *
    *

print_one('X', 3)
  X
  X
  X
  X
  X

print_one('$', 1) # default to 3 width
  $
  $
  $
  $
  $

Here's an example of running all of the functions and the resulting output:

print_zero('*', 5)
print()
print_one('*', 5)
print()
print_two('*', 5)
print()
print_three('*', 5)
print()
print_four('*', 5)
print()
print_five('*', 5)
print()
print_six('*', 5)
print()
print_seven('*', 5)
print()
print_eight('*', 5)
print()
print_nine('*', 5)
print()
print_plus('*', 5)
print()
print_minus('*', 5)

*****
*   *
*   *
*   *
*****

    *
    *
    *
    *
    *

*****
    *
*****
*
*****

*****
    *
*****
    *
*****

*   *
*   *
*****
    *
    *

*****
*
*****
    *
*****

*****
*
*****
*   *
*****

*****
    *
    *
    *
    *

*****
*   *
*****
*   *
*****

*****
*   *
*****
    *
    *

  *
  *
*****
  *
  *



*****

Part 3 - Create a function that checks an addition and subtraction operation
-----
Create a function called check_answer. It will will determine if a given 
addition or subtraction problem was solved correctly based on the operands, answer
and operator passed in. 

check_answer
* input:  
    * the 1st (or left) operand
    * the 2nd (or right) operand
    * the proposed answer
    * the operator... either + or -
* processing: 
    * runs the operator on the operands
    * checks against the proposed answer
    * if the operator isn't + or -, default to +
* output:     
    * returns a boolean - True if the answer matches the actual result of the calculation
      ...returns False otherwise

Example usage and output:

answer1 = check_answer(1, 2, 3, "+")
print(answer1)
answer2 = check_answer(1, 2, -1, "-")
print(answer2)
answer3 = check_answer(9, 5, 3, "+")
print(answer3)
answer4 = check_answer(8, 2, 4, "-")
print(answer4)
answer3 = check_answer(9, 5, 3, "*")
print(answer3)

True
True
False
False
False

Part 4 - Clean Up
-----
Clean up your finished file by doing the following:

* once you're certain that your functions are working the way you expect... 
* COMMENT OUT ALL OF YOUR TEST CODE! (so that running your file does not
  produce any output - we'll see better ways of doing this later)   
* ensure that your file and functions are all named properly
* add comments to your file (including your name, section and date at the 
  beginning)

This will prep the file for the next file in the homework, feeling_quizzy.py,
and it will help with grading. 

Extra Credit
-----

1 point - move your test code so that it runs when you run the file, but
not when you import this as a module (relevant for feeling_quizzy.py)
* at the end of this file... add:

# this means... if this file is the actual file being run...
if __name__ == '__main__':

* ... within that if statement, add all of your test code
* when you run the file (funcynum.py), your test code will run
* however, if you import this as a module in another file, your test 
  code will not run

2 points - implement multiplication 
* add the multiplication sign (can be something that resembles an X or *)
* amend your check_answer so that '*' doesn't cause addition, but instead
  checks for multiplication

"""




"""def horizontal_line(char, width, left_padding):
    line = " " * left_padding + char * width
    return line
    row = left_padding * ' '"""



"""def box(left_padding, char, width, height):
    this will draw a box composed of char
with (width) number of columns
and (height) number rows"""

"""box = ''
    return box"""
"""def box(left_pading,char,width,height):
    box = ''
    for row_num in range(height):
        row = ' ' * left_padding
        for col_num in range(width):"""
            



    
"""for row_num in range(height):
    row = ''
    for col_num in range(width):
        row += char
        box += row
        return row"""

"""print ('from funcynum.py,name is',__name__)
if __name__ == '__main__':
    

    print(horizontal_line('X',6,0))
    print(horizontal_line('+',3,10))





box = ''
for row_num in range(height):
    row = ' ' * left_padding
    for col_num in range(width):
        row += char
        box += row + '\n'
        return box

print(box(50, 'X', 3, 4))"""


"""def horizontal_line(char, width, left_padding):
    line = char * width
    row = left_padding * ' '
    return line"""


"""print (horizontal_line('$', 5, 10))"""

"""def vertical_line(char, height, left_padding, number, interior_offset):
    line = char * width"""
    



def horizontal_line(char, width, left_padding):
    line = " " * left_padding + char * width
    return line
    row = left_padding * ' '


"""print ('* *\n* *\n* *\n* *')"""



def vertical_lines(char, height, left_padding, number, interior_offset):
    assign = ''
    for row_num in range(height):
        counter = 0
        while counter < number:
            drawing += char + ' ' * interior_offset
            if counter == 0:
                assign += ' ' * left_padding
            counter += 1
        assign += '\n'
        if row_num == number - 1:
            assign += (' ' * left_padding + char + ' ' * interior_offset)
    return assign

"""print (vertical_lines('+', 4, 0, 5, 3))"""


def vertical_line(char, height, left_padding):
    assign = '\n'
    for row_num in range(height):
        assign += ' ' * left_padding + char
        if row_num < height - 1:
            assign += '\n'
    return assign

"""print (vertical_line('x', 4, 5))"""

def print_zero(char, width):
    if width < 3:
        width = 3
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 0) + horizontal_line(char, 1, 3))
    print (horizontal_line(char, 1, 0) + horizontal_line(char, 1, 3))
    print (horizontal_line(char, 1, 0) + horizontal_line(char, 1, 3))
    print (horizontal_line(char, 5, 0)) 
    
    
    

"""(print_zero('*', 5))
print ()"""


def print_one(char, width):
    if width < 3:
        width = 3
    print (vertical_line(char, 5, width - 1))
    

"""(print_one('*', 5))
print()"""

def print_two(char, width):
    if width < 3:
        width = 3
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 4))
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 0))
    print (horizontal_line(char, 5, 0))
    
"""(print_two('*', 5))
print ()"""

def print_three(char, width):
    if width < 3:
        width = 3
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 4))
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 4))
    print (horizontal_line(char, 5, 0))

"""(print_three('*', 5))
print()"""

def print_four(char, width):
    if width < 3:
        width = 3
    print (horizontal_line(char, 1, 0) + horizontal_line(char, 1, 3))
    print (horizontal_line(char, 1, 0) + horizontal_line(char, 1, 3))
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 4))
    print (horizontal_line(char, 1, 4))

    
"""(print_four('*', 5))
print()"""

def print_five(char, width):
    if width < 3:
        width = 3
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 0))
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 4))
    print (horizontal_line(char, 5, 0))

"""(print_five('*',5))
print()"""

def print_six(char, width):
    if width < 3:
        width = 3
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 0))
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 0) + horizontal_line(char, 1, 3))
    print (horizontal_line(char, 5, 0))

"""(print_six('*', 5))
print ()"""

def print_seven(char, width):
    if width < 3:
        width = 3
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 4))
    print (horizontal_line(char, 1, 4))
    print (horizontal_line(char, 1, 4))
    print (horizontal_line(char, 1, 4))

"""(print_seven('*', 5))
print ()"""

def print_eight(char, width):
    if width < 3:
        width = 3
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 0) + horizontal_line(char, 1, 3))
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 0) + horizontal_line(char, 1, 3))
    print (horizontal_line(char, 5, 0))

"""(print_eight('*', 5))
print ()"""

def print_nine(char, width):
    if width < 3:
        width = 3
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 0) + horizontal_line(char, 1, 3))
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 4))
    print (horizontal_line(char, 1, 4))

"""(print_nine('*', 5))
print()"""

def print_plus(char, width):
    if width < 3:
        width = 3
    print (horizontal_line(char, 1, 2))
    print (horizontal_line(char, 1, 2))
    print (horizontal_line(char, 5, 0))
    print (horizontal_line(char, 1, 2))
    print (horizontal_line(char, 1, 2))

"""(print_plus('*', 5))
print()"""

def print_minus(char, width):
    if width < 3:
        width = 3
    print (horizontal_line(char, 5, 0))

"""(print_minus('*', 5))
print ()"""




def check_answer(left_operand,right_operand, proposed_answer,operation):
    if operation == '+':
        total = left_operand + right_operand
        if total == proposed_answer:
            return True
        elif total != proposed_answer:
            return False
    elif operation == '-':
        total = left_operand - right_operand
        if total == proposed_answer:
            return True
        elif total != proposed_answer:
            return False
    elif operation != '+' and operation != '+':
        total = left_operand + right_operand
        if total == proposed_answer:
            return True
        elif total != proposed_answer:
            return False

"""answer1 = check_answer(1, 2, 3, '+')
print (answer1)"""



    
