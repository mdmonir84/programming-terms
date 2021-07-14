# Regular Expression 

## Writing Pattern 
Use raw text notation to build pattern ```r"\w+"```

### Pattern in Python 
- .       - Any Character Except New Line
- \d      - Digit (0-9)
- \D      - Not a Digit (0-9)
- \w      - Word Character (a-z, A-Z, 0-9, _)
- \W      - Not a Word Character
- \s      - Whitespace (space, tab, newline)
- \S      - Not Whitespace (space, tab, newline)

- \b      - Word Boundary
- \B      - Not a Word Boundary
- ^       - Beginning of a String
- $       - End of a String

- []      - Matches Characters in brackets
- [^ ]    - Matches Characters NOT in brackets
- |       - Either Or
- ( )     - Group

#### Quantifiers:
- *       - 0 or More
- +       - 1 or More
- ?       - 0 or One
- {3}     - Exact Number
- {3,4}   - Range of Numbers (Minimum, Maximum)

## Building Pattern Object 
Building pattern object using compile method 
prog = re.compile(pattern)

## Run the regex method
There is chance that output could come as group 


