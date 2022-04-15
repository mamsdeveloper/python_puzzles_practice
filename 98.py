"""
99. Write a Python program to find a string such that, when three or more spaces are compacted to a '-' and one or two spaces are replaced by underscores, leads to the target. 
Input: Python-Exercises
Output:
Python Exercises
Input: Python_Exercises
Output:
Python Exercises
Input: -Hello,_world!__This_is-so-easy!-
Output:
Hello, world! This is so easy! 
Click me to see the sample solution

"""


def test(strs):
    return strs.replace("-", " " * 3).replace("_", " ")


strs = "Python-Exercises"
print("Original strings:", strs)
print("Depth of groups of matched nested parentheses separated by parentheses:")
print(test(strs))
strs = "Python_Exercises"
print("\nOriginal strings:", strs)
print("Depth of groups of matched nested parentheses separated by parentheses:")
print(test(strs))
strs = "-Hello,_world!__This_is-so-easy!-"
print("\nOriginal strings:", strs)
print("Depth of groups of matched nested parentheses separated by parentheses:")
print(test(strs))
