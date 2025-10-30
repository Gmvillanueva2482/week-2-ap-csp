#Working with Strings
# ----------------------------------------


# Strings are sequences of characters enclosed in quotes (' ' or " ")
greeting = "Hello" # string data type
name = "World" # string data type


# ----------------------------------------
# Basic String Operations
# ----------------------------------------


# 1. Concatenation: Combining strings using the + operator
message = greeting + " " + name
print("Concatenated String:", message)  # Output: Hello World


# ----------------------------------------
# 2. String Functions
# ----------------------------------------


phrase = "Python is FUN!"
name = "Giovanni"
phrase2 = "SUPERCAGEFRAGUSLISTCIOUS"


# # Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!
print("Name Lowercase:", name.lower())  # Output: Giovanni
print(" Pharse2 Lowercase:", phrase2.lower())  # Output: SUPERCAGEFRAGUSLISTCIOUS


# # Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!
print("Name Uppercase:", name.upper())  # Output: GIOVANNI
print(" Pharse2 Uppercase:", phrase2.upper())  # Output: SUPERCAGEFRAGUSLISTCIOUS


# # Check if all characters are uppercase
print("Is Uppercase?", phrase.isupper())  # Output: False
print("Is Uppercase?", name.isupper())  # Output: False


# # Find the length of the string
# print("Length of phrase:", len(phrase))  # Output: 14


# # ----------------------------------------
# # 3. Indexing and Slicing
# # ----------------------------------------
declaration_of_independence="The Declaration of Independence is the 1776 document that announced the Thirteen Colonies' separation from Great Britain, establishing them as free and independent states Written primarily by Thomas Jefferson, it outlines the reasons for separation based on Enlightenment principles and lists grievances against the British Crown, with the main message being that all men are created equal and endowed with rights to life, liberty, and the pursuit of happiness. The document was adopted by the Second Continental Congress on July 4, 1776, and its original parchment is now housed in Washington, D.C.  "
print(len(declaration_of_independence))
chicago_mayor="Johnson"
#index slicing
print(chicago_mayor[0])
#get the last letter
print(chicago_mayor[-1])
#get the "s" in the string
print(chicago_mayor[4])
#slicing
#get the "son" from the start
print(chicago_mayor[ 4:-1 ])
#the first number is slicing is inclusing
#the second nukmber is exclusive 
# get the string"John"
print(chicago_mayor[0:4])
print(chicago_mayor[0:-3])
#get "ohns"
print(chicago_mayor[1:-2])
# when we get one character/letter
#its called string indexing
#when we get a chunk of letters
#from a string, its called
#string slicing


phrase3 ="Supercagifragilstic"
#upper case it
print(" Pharse3 Uppercase:", phrase2.upper())
# slice super out of it into a different variable
cut= phrase3 [0:5]
print(cut)
#slice cagi out of phase4 into its own variable 
cut2=phrase3 [5:9]
print(cut2)
#print out the last letter







# # Indexing: Access characters by position (0-based index)
# print("First character:", phrase[0])  # Output: P
# print("Last character:", phrase[-1])  # Output: !


# # Slicing: Get a range of characters (start inclusive, end exclusive)
# print("Characters 1 to 4:", phrase[1:4])  # Output: yth


# # Example combining everything:
# print("Formatted Example:", (greeting + " " + name + "!").upper())
# # Output: HELLO WORLD!




# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------


# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"


# # Printing Strings
# print(greeting1)
# print(greeting2)


# # ----------------------------------------
# # String Methods
# # ----------------------------------------


# sentence = "Python is fun to learn"


# # .split(): Splits the string into a list of words
# words = sentence.split()
# print("Split result:", words)


# # .format(): Allows inserting values into strings using {}
# name = "Marvin"
# age = 35
# intro = "My name is {} and I am {} years old.".format(name, age)
# print(intro)


# # You can also use f-strings (Python 3.6+)
# intro_fstring = f"My name is {name} and I am {age} years old."
# print(intro_fstring)

