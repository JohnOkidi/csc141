'''


John Okidi
Python is hard at times
difficulty 8/10
'''
# Create an expanded glossary dictionary of programming terms
glossary = {
    'dictionary': 'A collection of key-value pairs used to store related data.',
    'list': 'A collection of items stored in a particular order.',
    'loop': 'A block of code that repeats a set of instructions multiple times.',
    'string': 'A series of characters enclosed in quotation marks.',
    'variable': 'A container used to store data values in a program.',
    'conditional test': 'An expression that evaluates to True or False.',
    'key-value pair': 'A set of associated values where a key is connected to a value.',
    'boolean': 'A data type with only two values: True or False.',
    'tuple': 'An immutable list that cannot be changed after its creation.',
    'comment': 'Notes left in code for human readers that Python ignores.'
}

# Loop through the dictionary and print each word and meaning
for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")