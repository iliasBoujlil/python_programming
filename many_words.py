"""
many_words.py - 4 points
=====
Write a program that asks for a number... and then proceeds to ask for that 
number of words. The program should print the words in reverse order at the end
of the program. 

Hint 1: if you use a for loop to do this, but make the end of the loop flexible
        (a while loop is also a valid way of implementing this)
Hint 2: try accumulating the words and printing at the very end 
        (if you accumulate, what should the intitial value be?)
Hint 3: changing the order of operands when concatenating strings may be 
        helpful (this pretty much gives away the solution!)

Example Output:
-----
How many words?
> 5
Word please!
> program
Word please!
> amazing
Word please!
> my
Word please!
> out
Word please!
> check
check out my amazing program
"""
amount = int(input("How many words \n>"))
acc = ""
while amount > 0:
    word = input("Word please! \n> ")
    amount -= 1
    acc = word + acc
print (acc)
    
    
    
