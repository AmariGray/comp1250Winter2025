"""
Function:
    a named entity that stores
    steps to complete
    May have parameters: alter/vary behaviour of function
"""


def substring_counter(string:str, substring:str)->int:
    """
    This function returns the number of occurences of a substring inside the string

    :type string str
    :type substring str
    :rtype int
    :param string: the main string to search
    :param substring: the characters to count in main string
    :return: an integer value representing the number of occurrences of substring of string


    """
    if isinstance(string, str) and isinstance(substring, str):
        return string.count(substring)


result = substring_counter("Hello World", "o")
print(result)
result1 = substring_counter(1, 1.2)
print(result1)

