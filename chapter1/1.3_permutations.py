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


print are_permutations("aba", "aab") is True
print are_permutations("asd", "gfd") is False
