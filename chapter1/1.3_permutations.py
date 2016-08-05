"""
Problem 1.3: Given 2 strings, write a method to
decide if one is a permutation of the other.
"""


def are_permutations(str1, str2):
    """
    Time complexity: depends on soring algorithm
    Space complexity: depends if we take into account the sorted
                      arrays returned by the sorted function
    """
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


def are_permutations_1(word, other_word):
    """
    Time complexity: 0(n)
    Space complexity: 0(1)
    """
    if len(word) != len(other_word):
        return False

    # Assumption: always check with the interviewer the size of the character set!!!
    letters = [0] * 256

    for char in word:
        letters[ord(char)] += 1

    for char in other_word:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False

    return True


print are_permutations("aba", "aab") is True
print are_permutations("asd", "gfd") is False

print are_permutations_1("vamb", "Badm") is False
print are_permutations_1("abba", "baba") is True
