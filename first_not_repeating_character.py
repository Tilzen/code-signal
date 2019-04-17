"""
Given a string s consisting of small English letters, find and return the first
instance of a non-repeating character in it. If there is no such character,
return '_'.

=== Example ===

for:
    s = "abacabad"

the output should be:
    firstNotRepeatingCharacter(s) = 'c'.
"""

def first_not_repeating_character(string):
    while string:
        string_length = len(string)
        char = string[0]
        string = string.replace(char, '')

        if string_length-1 == len(string):
            return char
            break
    else:
        return '_'


if __name__ == '__main__':
    # tests
    print(first_not_repeating_character("abacabad")) # c
    print(first_not_repeating_character("bcccccccb")) # _
