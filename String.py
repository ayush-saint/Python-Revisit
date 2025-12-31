#Single quotes '...' Used for short strings Example: 'Hello'
#Double quotes "..." Works the same as single quotes Useful if your string contains a single quote: "I'm happy"
#Triple quotes/multiline '''...''' or """...""" Used for multi-line strings or docstrings

singlequotestring = 'hello'
doublequotestring = "hello o"
triplequotestring = '''hello o o'''

#accessing character from string (counting starts from 0)
print(singlequotestring[0])

#slicing the string (counting starts form 1)
#gaves first n character 
print(singlequotestring[:3])
print(singlequotestring[-1])#also called as negative indexing 

#string concatanation
print(singlequotestring+" "+doublequotestring)

#string repetition
print(triplequotestring*5)

#string length 
print(len(triplequotestring))

#cheaking substring(part of string)
print("o" in triplequotestring)

#string functions(len, upper, lower, strip, replace → Length, Change Case, Clean, and Replace text)
print(triplequotestring.upper())

#String formatting 
name = "David"
print(f"my name is {name}")  