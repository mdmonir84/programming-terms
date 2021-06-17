# Java string 

## Common method (Set-1)
Extraction 
  - charAt()	Returns the character at the specified index (position)	char
  - codePointAt()	Returns the Unicode of the character at the specified index	int
  - codePointBefore()	Returns the Unicode of the character before the specified index	int
  - codePointCount()	Returns the Unicode in the specified text range of this String	int
  - compareTo()	Compares two strings lexicographically	int
  - compareToIgnoreCase()	Compares two strings lexicographically, ignoring case differences	int
  - contains()	Checks whether a string contains a sequence of characters	boolean
  - contentEquals()	Checks whether a string contains the exact same sequence of characters of the specified CharSequence or StringBuffer	boolean
  - copyValueOf()	Returns a String that represents the characters of the character array	String
  - startsWith()/endsWith():	Checks whether a string starts/ends with the specified character(s)	boolean
  - equals()	Compares two strings. Returns true if the strings are equal, and false if not	boolean
  - equalsIgnoreCase()	Compares two strings, ignoring case considerations	boolean
  - format()	Returns a formatted string using the specified locale, format string, and arguments	String
  - getBytes()	Encodes this String into a sequence of bytes using the named charset, storing the result into a new byte array	byte[]
  - getChars()	Copies characters from a string to an array of chars	void
  - hashCode()	Returns the hash code of a string	int
  - indexOf()	Returns the position of the first found occurrence of specified characters in a string	int
 - intern()	Returns the canonical representation for the string object	String
  - isEmpty()	Checks whether a string is empty or not	boolean
  - lastIndexOf()	Returns the position of the last found occurrence of specified characters in a string	int
  - matches()	Searches a string for a match against a regular expression, and returns the matches	boolean
  - offsetByCodePoints()	Returns the index within this String that is offset from the given index by codePointOffset code points	int
 - regionMatches()	Tests if two string regions are equal	boolean


## Common method (Set-2)
Manipulation
  - subSequence()	Returns a new character sequence that is a subsequence of this sequence	CharSequence
  - concat():	Appends a string to the end of another string	String
  - replace():	Searches a string for a specified value, and returns a new string where the specified values are replaced	String
  - replaceFirst():	Replaces the first occurrence of a substring that matches the given regular expression with the given replacement	String
  - replaceAll():	Replaces each substring of this string that matches the given regular expression with the given replacement	String
  - split():	Splits a string into an array of substrings	String[]
  - toString():	Returns the value of a String object	String
  - toUpperCase()/toLowerCase(): Converts a string to upper/lower case letters	String
  - trim():	Removes whitespace from both ends of a string	String
  - toCharArray():	Converts this string to a new character array	char[]
  - valueOf():	Returns the string representation of the specified value	String

## Common method (Set-3)
Array property
  - length(): Returns the length of a specified string	int

## Common method (Set-4)
Array slicing 
  - substring(): Extracts the characters from a string, beginning at a specified start position, and through the specified number of character	String