#9.	Write a program to demonstrate String function.

string = "Hello, World!"
print("Original String:", string)
print("Length of String:", len(string))
print("String in Uppercase:", string.upper())
print("String in Lowercase:", string.lower())
print("String with replaced character:", string.replace("World", "Python"))
print("String Split into List:", string.split(", "))
print("String Concatenation:", string + " How are you?")
print("String Slicing:", string[0:5])  # Slicing the first 5 characters
print("String Count of 'o':", string.count("o"))
print("String Find 'World':", string.find("World"))
print("String Index of 'W':", string.index("W"))
print("String Strip:", string.strip("!"))  # Removing '!' from the end
print("String Starts with 'Hello':", string.startswith("Hello"))
print("String Ends with 'World!':", string.endswith("World!"))
print("String Is Alphanumeric:", string.isalnum())  # Check if all characters are alphanumeric
print("String Is Alphabetic:", string.isalpha())  # Check if all characters are alphabetic
print("String Is Numeric:", string.isnumeric())  # Check if all characters are numeric
print("String Is Decimal:", string.isdecimal())  # Check if all characters are decimal
print("String Is Title:", string.istitle())  # Check if the string is title cased
print("String Is Lower:", string.islower())  # Check if all characters are lowercase
print("String Is Upper:", string.isupper())  # Check if all characters are uppercase
print("String Is Space:", string.isspace())  # Check if all characters are whitespace
print("String Is Print:", string.isprintable())  # Check if all characters are printable
print("String Is Identifier:", string.isidentifier())  # Check if the string is a valid identifier