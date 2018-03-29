"""
Ilias Boujlil
2/10/2018
Section 002

triangle_or_not.py - (6 points)
=====
Ask the user for 3 points on the coordinate plane. Calculate the distances
between each comination of points (that is, the length of each potential side
of a triangle), and use those calculations to determine whether or not the
points make a valid triangle.

1. Ask the user for the x and y coordinates of 3 points, for example:
   Enter point #1 x:
   * assume that all inputs are ints
   * you do not have to do any input validation
2. Calculate and output the length of each side (the distances between each
   points).
   * You can assume that Side #1 is composed of points 1 and 2, Side #2 is 2
     and 3, and Side #3 is 3 and 1
   * Look up the distance forumla; it involves square root. __YOU MUST USE THE
     MATH MODULE'S__ sqrt function to do this: math.sqrt(100) -> 10 (remember
     to import math first)
   * Output the length of each side: Side #1: <value>
3. Finally, determine if the points create a valid triangle...
   * Side #1 + Side #2 must be longer than Side 3
   * Side #2 + Side #3 must be longer than Side 1
   * Side #3 + Side #1 must be longer than Side 2
   * Output whether or nota valid triangle is formed:
     a. YOU HAZ TRIANGLE
     b. Nope, not a triangle.

Example Interaction 1:
-----
Enter point #1 x: 0
Enter point #1 y: 0
Enter point #2 x: 100
Enter point #2 y: 0
Enter point #3 x: 50
Enter point #3 y: 2
Side #1     100.00
Side #2      50.04
Side #3      50.04
YOU HAZ TRIANGLE

Example Interaction 2:
-----
Enter point #1 x: 0
Enter point #1 y: 0
Enter point #2 x: 10
Enter point #2 y: 10
Enter point #3 x: 1
Enter point #3 y: 0
Side #1      14.14
Side #2      13.45
Side #3       1.00
YOU HAZ TRIANGLE

Example Interaction 3:
-----
Enter point #1 x: 0
Enter point #1 y: 0
Enter point #2 x: 50
Enter point #2 y: 50
Enter point #3 x: 100
Enter point #3 y: 100
Side #1      70.71
Side #2      70.71
Side #3     141.42
Nope, not a triangle
"""

xpoint1 = int(input("Enter point #1 x: "))
ypoint1 = int(input("Enter point #1 y: "))
xpoint2 = int(input("Enter point #2 x: "))
ypoint2 = int(input("Enter point #2 y: "))
xpoint3 = int(input("Enter point #3 x: "))
ypoint3 = int(input("Enter point #3 y: "))
import math
side1 = float(format(math.sqrt((xpoint2-xpoint1)**2 + (ypoint2-ypoint1)**2),'.2f'))
side2 = float(format(math.sqrt((xpoint3-xpoint2)**2 + (ypoint3-ypoint2)**2),'.2f'))
side3 = float(format(math.sqrt((xpoint1-xpoint3)**2 + (ypoint1-ypoint3)**2),'.2f'))
print (format("Side #1:",'<5'),format(side1,'>10'))
print (format("Side #2:",'<5'),format(side2,'>10'))
print (format("Side #3:",'<5'),format(side3,'>10'))
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 >side2:
    print ("YOU HAZ A TRIANGLE")
else:
    print ("Nope, not a triangle")
