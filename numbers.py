"""
numbers.py (5 points)
=====
Write a program that outputs the number in the thousands, hundreds, tens and 
ones places of a number. 

1. Ask the user for a number
2. Calculate the numbers in the thousands, hundreds, tens and ones places
3. Output each place
4. One soution is to use some numeric operators to determine each place 
   (maybe % and // may help)
5. You may have to calculate each place separately
6. Don't worry about input that's not a positive whole number below 10,000

Example Output - Everything after the greater than sign (>) is user input:

Please enter a number
> 256

0 thousands
2 hundreds
5 tens
6 ones
"""
number = input("Please enter a number\n>")
places = int(number)
thousands = (places // 1000)
hundreds = (places // 100) % 10
tens = (places // 10) % 10
ones = (places % 10) 
print (thousands,"thousands")
print (hundreds,"hundreds")
print (tens,"tens")
print (ones,"ones")

    
