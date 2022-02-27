"""
22. Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string. 
Input:
PytHon ExerciSEs
Output:
373
Input:
JavaScript
Output:
157
Click me to see the sample solution

"""


def test(strs):
    return sum(map(ord, filter(str.isupper, strs)))


strs = "PytHon ExerciSEs"
print("Original strings:")
print(strs)
print("Sum of the ASCII values of the upper-case characters in the said string:")
print(test(strs))
strs = "JavaScript"
print("\nOriginal strings:")
print(strs)
print("Sum of the ASCII values of the upper-case characters in the said string:")
print(test(strs))
