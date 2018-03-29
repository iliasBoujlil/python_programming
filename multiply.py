"""


multiply.py (3 points)
=====
Write a program that:

* asks the user for a number
* prints out a table of that number multiplied by the first 7 prime numbers:  
  2, 3, 5, 7, 11, 13, 17
* it will format the output so that the original number and the prime number are
  left aligned
* the product is right aligned
  * when using format, don't change the width to align the product
  * keep the width constant
* __COMMENT YOUR SOURCE CODE__ by 
   * briefly describing parts of your program 
   * include your name, the date, and your class section at top of your file 
     (above everything else)

Example interaction (everything after > is user input):
-----
Give me a number
> 17
17 * 2             34
17 * 3             51
17 * 5             85
17 * 7            119
17 * 11           187
17 * 13           221
17 * 17           289
"""

answer = input('Give me a number\n> ')
number = int(answer)
right_col_format = '>10'
left_col_format = '<12'
print (format(answer + " * 2",left_col_format), format(number * 2, right_col_format))
print (format(answer + " * 3",left_col_format), format(number * 3, right_col_format))
print (format(answer + " * 5",left_col_format), format(number * 5, right_col_format))
print (format(answer + " * 7",left_col_format), format(number * 7, right_col_format))
print (format(answer + " * 11",left_col_format), format(number * 11, right_col_format))
print (format(answer + " * 13",left_col_format), format(number * 13, right_col_format))
print (format(answer + " * 17",left_col_format), format(number * 17, right_col_format))
