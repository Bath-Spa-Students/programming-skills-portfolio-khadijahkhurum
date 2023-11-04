# Create a glossary of programming terms
glossary = {
    "Variable": "A named storage location in a program's memory for storing data.",
    "Function": "A named block of code that performs a specific task or operation.",
    "Loop": "A control structure that allows a program to repeatedly execute a block of code.",
    "Conditional Statement": "A control structure that allows a program to make decisions and choose different actions based on conditions.",
    "List": "A collection of ordered and mutable elements, typically of the same data type.",
    "Dictionary": "A collection of key-value pairs used to store and retrieve data efficiently.",
    "Tuple": "An ordered, immutable collection of elements often used for grouping related data.",
    "Module": "A file containing Python code that can be imported and used in other programs.",
    "String": "A sequence of characters, often used for representing text in Python.",
    "Method": "A function that is associated with an object and can be called on that object."
}

# Print each word and its meaning with a blank line between each pair
for term, definition in glossary.items():
    print(f"{term}:\n{definition}\n")
