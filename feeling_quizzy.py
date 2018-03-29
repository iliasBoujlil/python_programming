"""
Ilias Boujlil
3/22/2018
Section 002

feeling_quizzy.py (9 points)
=====
Use the functions from your file, funcynum, to create a math quiz.

* save this file, feeling_quizzy.py IN THE SAME DIRECTORY AS funcynum.py
* at the very top of this file, import your functions from funcynum.py by:

import funcynum

* now you can use your functions by prefixing with your module name (just
  like using random.randint(a, b) or math.sqrt(25):

funcynum.print_two('*', 5)

Your math quiz program will ask for some parameters to the game... and then
it will display a series of addition and subtractions questions using your
library of print_xxxxxx functions from funcynum.py. It will ask for an answer
and check that answer using your check_answer function from funcynum.py. At
the end, it will show the percentage of correct answers.

* make sure that you've imported funcynum
* ask for how many quiz problems: 'How many problems?'
    * if the number of problems is not between 3 and 20 inclusive...
    * say: 'Please enter a number between 5 and 20...', and ask again
* ask for a character to use for the game: 'What character do you want the 
  numbers to be made of?'
    * if the character is composed of more than one character, say: 'Please 
      enter a single character!', and ask again
* finally, ask for the width of each number...
    * default to 3 if the width entered is less than 3 by saying: 'Oops... 
      defaulting to width 3'
* to ask addition and subtraction questions...
    * generate two random numbers for each operand
    * generate a random operation, either addition or subtraction
    * print out the problem using your print_xxxxxx functions
    * ask the user for an answer
    * check if the answer is correct
        * if it's not correct, print out the correct answer
        * if it is correct, print out 'Correct!'
* display the percent correct (formatted 2 decimal places) and how many they
  answered correctly out of the total number of questions

An example game is below. Note the validation that occurs for the number of
problems and the characters...
      
How many problems?
> 2
Please enter a number between 5 and 20...
How many problems?
> 3
What character do you want the numbers to be made of?
> ccc
Please enter a single character!
What character do you want the numbers to be made of?
> X
How wide do you want each number to be?
> 3

 What is ...
XXX
X X
XXX
  X
  X

 X
 X
XXX
 X
 X

  X
  X
  X
  X
  X
 = 10
Correct!

 What is ...
XXX
  X
XXX
  X
XXX



XXX



XXX
X X
XXX
  X
  X
 = -6
Correct!

 What is ...
XXX
X
XXX
  X
XXX

 X
 X
XXX
 X
 X

XXX
X X
XXX
  X
  X
 = 10
Nope, the answer is 14
You got  66.67% correct (2 out of 3)
"""
import funcynum
import random
num_of_probs = int(input("How many problems?\n>"))
while num_of_probs < 3 or num_of_probs > 20:
    num_of_probs = int(input("Please enter a number between 5 and 20..."))
character = input("What character do you want the numbers to be made of?\n>")
while len(character) > 1:
    character = input("Please enter a single character!")
width = int(input("How wide do you want each number to be?\n>"))
if width < 3:
    width = 3
    print ("Oops...defaulting to width 3")


total = 0
for i in range(1,num_of_probs + 1):
    print ("What is...")
    random1 = random.randint(0,9)
    random2 = random.randint(0,9)
    randomsign = random.randint(0,1)

    if random1 == 1:
        funcynum.print_one(character,width)
    elif random1 == 2:
        funcynum.print_two(character,width)
    elif random1 == 3:
        funcynum.print_three(character,width)
    elif random1 == 4:
        funcynum.print_four(character,width)
    elif random1 == 5:
        funcynum.print_five(character,width)
    elif random1 == 6:
        funcynum.print_six(character,width)
    elif random1 == 7:
        funcynum.print_seven(character,width)
    elif random1 == 8:
        funcynum.print_eight(character,width)
    elif random1 == 9:
        funcynum.print_nine(character,width)
    elif random1 == 0:
        funcynum.print_zero(character,width)

    print("\n")
    
    if randomsign == 0:
        funcynum.print_minus(character, width)
    elif randomsign == 1:
        funcynum.print_plus(character,width)

    print("\n")

    if random2 == 1:
        funcynum.print_one(character,width)
    elif random2 == 2:
        funcynum.print_two(character,width)
    elif random2 == 3:
        funcynum.print_three(character,width)
    elif random2 == 4:
        funcynum.print_four(character,width)
    elif random2 == 5:
        funcynum.print_five(character,width)
    elif random2 == 6:
        funcynum.print_six(character,width)
    elif random2 == 7:
        funcynum.print_seven(character,width)
    elif random2 == 8:
        funcynum.print_eight(character,width)
    elif random2 == 9:
        funcynum.print_nine(character,width)
    elif random2 == 0:
        funcynum.print_zero(character,width)
    print("\n")

    answer = int(input("= "))
    if randomsign == 0:
        final = random1 - random2
        if answer == final:
            print ("Correct!")
            total += 1
        elif answer != final:
            print ("Nope, the answer is",final)
    elif randomsign == 1:
        final = random1 + random2
        if answer == final:
            print ("Correct!")
            total += 1
        elif answer != final:
            print ("Nope, the answer is",final)
print()           
print ("You got", format(((total / num_of_probs) * 100),'.2f') + '%', '( %s out of %s)' % (total,num_of_probs))
        
            
    
    



