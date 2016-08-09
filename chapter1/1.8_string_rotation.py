"""
Problem 1.8: Assume you have a method substring that checks if
one word is a substring of another. Given two strings, s1 and s2,
write code to check if s2 is a rotation of s1 using only one call
to isSubstring
"""


def is_substring(a_string, substring):
    return substring in a_string


def is_rotation(string_1, string_2):
    if not string_1 or not string_2 or len(string_1) != len(string_2):
        return False
    return is_substring(string_1 + string_1, string_2)


print is_rotation("bb", "b")
print is_rotation("waterbottle", "erbottlewat")
