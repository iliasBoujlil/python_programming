"""
Ilias Boujlil
3/24/2018
Section 002

pig_latin.py (6 points)
=====

Write a function called to_pig_latin that translates a word into pig latin. 

http://en.wikipedia.org/wiki/Pig_Latin

IPO for to_pig_latin function
-----
input (parameters): a string
processing: convert the string into pig latin
output (return value): a new string (in pig latin)

Our version of Pig Latin will follow these rules:
-----
* _IGNORE ANY STRING WITH NON-LETTER CHARACTERS_ (including spaces); it should
  just return the original string
* _THIS FUNCTION WILL NOT BREAK A STRING INTO SEPARATE WORDS_
* all letters automatically get converted to lowercase (just for implementation
  convenience)
* single letter words remain the same: "a" -> "a"
* any strings with non letter characters (including punctuation, numbers, white
  space) remain the same: "u mad bro" -> "u mad bro", "42" -> "42", "!" -> "!"
* empty string returns empty string: "" -> ""
* words that start with vowels just have "way" appended to them: "at" -> "atway"
* HINT - how to check for vowels? you can check if a character exists within a 
  string of all vowels
* words that start with sh, ch, th or qa have those two letters removed from 
  the beginning of the word, added to the end of the word, with "ay" added at 
  the end: "chillax" -> "illaxchay", "thimble" -> "imblethay"
* all other words (that start with a consonant, are greater than one letter in
  length, and only contain letters) will have the consonant taken away from 
  the front of the word, appended to the end of the word, with "ay" added to 
  the end: "yolo" -> "oloyay", "narwhal" -> "arwhalnay"
* write at least 4 assertions to test your program (use the conditions above as
  a guide)

Example:
-----
print(to_pig_latin(s))
# prints out...
"""

def to_pig_latin(s):
    s = str(s)
    s.lower()
    acc = ''
    if s.isnumeric() == True:
            return s
    elif s.isdigit() == True:
        return s
    elif s.isspace() == True:
        return s
    elif s.isalpha() == True:
        if s[0] in ['a','e','i','o','u']:
            return s + 'way'
        elif s[0] + s[1] in ['sh','ch','th','qa']:
            return s[2:] + s[0:2] + 'ay'
        elif s[0] not in ['a','e','i','o','u']:
            return s[1:] + s[0] + 'ay'
    elif s.isalpha() == False:
        return s
    

print(to_pig_latin("chillax"))
        
