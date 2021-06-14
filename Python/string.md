# Python string 

## Common method (Set-1)
Based on basic string property 
- find(“string”, beg, end) :- This function is used to find the position of the substring within a string.
    - It takes 3 arguments, substring , starting index( by default 0) and ending index( by default string length).
    - It returns “-1 ” if string is not found in given range.
    - It returns first occurrence of string if found.
- rfind(“string”, beg, end) :- This function has the similar working as find(), but it returns the position of the last occurrence of string.
- min/max(“string”) :- This function returns the minimum/maximum value alphabet from string
- startswith/endswith(“string”, beg, end) :- The purpose of this function is to return true if the function begins/ends with mentioned string(prefix/suffix) else return false.
- islower/isupper(“string”) :- This function returns true if all the letters in the string are lower/upper cased, otherwise false.
- isalpha()/isspace() :- This function returns true when all the characters in the string are alphabets/spaces else returns false.
- isalnum() :- This function returns true when all the characters in the string are combination of numbers and/or alphabets else returns false.

## Common method (Set-2)
String manipulation/conversion
- lower()/uppwer() :- This function returns the new string with all the letters converted into its lower/upper case.
- swapcase() :- This function is used to swap the cases of string i.e upper case is converted to lower case and vice versa.
- title() :- This function converts the string to its title case i.e the first letter of every word of string is upper cased and else all are lower cased.
- center() :- This function is used to surround the string with a character repeated both sides of string multiple times. 
    - By default the character is a space. Takes 2 arguments, length of string and the character.
- ljust()/rjust() :- This function returns the original string shifted to left/right that has a character at its right/left. It left/right adjusts the string. 
    - By default the character is space. It also takes two arguments, length of string and the character.
- strip() :- This method is used to delete all the leading and trailing characters mentioned in its argument.
- lstrip()/rstrio() :- This method is used to delete all the leading/trailing  characters mentioned in its argument.
- maketrans() :- It is used to map the contents of string 1 with string 2 with respective indices to be translated later using translate()
- translate() :- This is used to swap the string elements mapped with the help of maketrans()
- replace() :- This function is used to replace the substring with a new substring in the string. 
    - This function has 3 arguments. The string to replace, new string which would replace and max value denoting the limit to replace action (by default unlimited).
- expandtabs() :- It is used to replace all tab characters(“\t”) with whitespace or simply spaces using the given tab size, which is optional to supply.

## Common method (Set-3)
Based on string as list of character 
- len() :- This function returns the length of the string.
- count(“string”, beg, end) :- This function counts the occurrence of mentioned substring in whole string. 
    - This function takes 3 arguments, substring, beginning position( by default 0) and end position(by default string length).
- join() :- This function is used to join a sequence of strings mentioned in its arguments with the string.