def counterpartCharCode(char):
    if char.islower():
        return ord(char.upper())
    elif char.isupper():
        return ord(char.lower())
    else:
        # Return the char code as it is for non-alphabetic characters
        return ord(char)

# Examples
print(counterpartCharCode("A"))  # Output: 97
print(counterpartCharCode("a"))  # Output: 65
