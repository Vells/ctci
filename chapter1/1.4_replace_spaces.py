"""
Problem 1.4: Write a method to replace all spaces in a string with %20

You can assume the string has sufficient space at the end of the string
to hold the additional characters and that the true length of the string is given.

Note: the assumptions are there to help non-Python implementations!
"""


def urlify_string(a_string):
    stripped = a_string.strip()
    return stripped.replace(" ", "%20")


def urlify_string_1(a_string):
    return "%20".join(a_string.strip().split(' '))


def urlify_string_2(a_string):
    return "".join(['%20' if character == ' ' else character
                    for character in a_string.strip()])


print urlify_string('a   g')
print urlify_string(' ab   ')
print urlify_string_1('a   g')
print urlify_string_1(' ab   ')
print urlify_string_2('a   g')
print urlify_string_2(' ab   ')
