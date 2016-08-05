"""
Problem 1.1: Implement an algorithm to determine
if a string has all unique characters
"""


def unique_characters(a_string):
    """
    Space complexity: O(1)
    TIme complexity: O(n)
    """
    if a_string is None:
        return False

    if len(a_string) > 256:
        return False

    unique_chars = [False] * 256

    for letter in a_string:
        if unique_chars[ord(letter)]:
            return False
        unique_chars[ord(letter)] = True

    return True


def unique_characters_2(a_string):
    return len(set(a_string)) == len(set(a_string))


print unique_characters('a') is True
print unique_characters('aa') is False
print unique_characters('  ') is False

print unique_characters_2('a') is True
print unique_characters_2('aa') is False
print unique_characters_2('') is True
