'''  

John Okidi
Python is fun 
difficulty 8/10

'''

# Create a glossary dictionary of programming terms
glossary = {
    'dictionary': 'A collection of key-value pairs used to store related data.',
    'list': 'A collection of items stored in a particular order.',
    'loop': 'A block of code that repeats a set of instructions multiple times.',
    'string': 'A series of characters enclosed in quotation marks.',
    'variable': 'A container used to store data values in a program.'
}

# Print each word and its meaning with an indented meaning and a blank line
for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")