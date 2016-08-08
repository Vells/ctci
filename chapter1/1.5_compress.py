"""
Problem 1.5: Implement function to a string to perform basic string
compression using the counts of repeated characters. If the compressed
string would not become smaller than the original, the function
should return the original string.
"""


def calculate_compressed_length(a_string):
    """
    A method that calculates the length of a compressed string

    Space complexity: O(1)
    Time complexity: O(n)
    """
    if len(a_string) <= 1:
        return 2

    total = 0
    count = 0
    prev = a_string[0]

    for character in a_string:
        if character == prev:
            count += 1
        else:
            total += 1 + len(str(count))
            prev = character
            count = 1

    return total + 1 + len(str(count))


def compress(a_string):
    """
    Space complexity: 0(n)
    Time complexity: O(n)
    """
    if not a_string or len(a_string) <= 1:
        return a_string

    if len(a_string) <= calculate_compressed_length(a_string):
        return a_string

    compressed = []
    prev = a_string[0]
    count = 0

    for character in a_string:
        if character == prev:
            count += 1
        else:
            compressed += [prev, str(count)]
            prev = character
            count = 1

    compressed += [prev, str(count)]
    return "".join(compressed)


print calculate_compressed_length('')
print calculate_compressed_length('aaaaaaaagjgoergeri')
print calculate_compressed_length('aaaaaaaaaa')
print calculate_compressed_length('aaabbb')

print compress('')
print compress('aaaaaaaagjgoergeri')
print compress('ab')
print compress('aaabbb')
print compress('aaaaaaaaaa')
print compress('aabbbbcccddddeeee')
