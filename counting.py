"""
Ilias Boujlil
2/17/2018
Section 002

counting.py - 2 points
=====

use *while* loops to do the following:

* print out "while loops"
* use a while loop to count from 2 up-to and including 10 by 2's.
* use another while loop to count down from 5 down to 1


use *for* loops to do the following:

* print out "for loops"
* use a for loop to count from 2 up-to and including 10 by 2's.
* use another for loop to count from 5 down to 1.

* comment your code (name, date and section on top, along with appropriate 
  comments in the body of your program)

example output:

while loops
2
4
6
8
10
5
4
3
2
1
for loops
2
4
6
8
10
5
4
3
2
1
"""

print ("While loops")
n = 2
end = 10
delta = 2
while n <= end:
    print (n)
    n += delta
m = 5
new_end = 1
omega = 1
while m >= 1:
    print (m)
    m -= omega

print ("for loops")
for i in range (2,11,2):
    print (i)
for i in range (5,0,-1):
    print (i)
