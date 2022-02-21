"""
8. Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators. 
Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
Input: The dance, held in the school gym, ended at midnight.
Output:
[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
Input: The colors in my studyroom are blue, green, and yellow.
Output:
[['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]
Click me to see the sample solution

"""


def test(string):
    import re
    merged = re.split(r"([ ,]+)", string)
    return [merged[::2], merged[1::2]]


s = "W3resource Python, Exercises."
print("Original string:", s)
print("Split the said string into 2 lists: words and separators:")
print(test(s))
s = "The dance, held in the school gym, ended at midnight."
print("\nOriginal string:", s)
print("Split the said string into 2 lists: words and separators:")
print(test(s))
s = "The colors in my studyroom are blue, green, and yellow."
print("\nOriginal string:", s)
print("Split the said string into 2 lists: words and separators:")
print(test(s))
