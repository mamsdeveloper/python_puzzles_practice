"""
33. Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string. 
Input: w3rEsOUrcE 
Output:
[6]
Input: AEIOUYW 
Output:
[0, 2, 4]
Click me to see the sample solution

"""


def test(strs):
    return [i for i, c in enumerate(strs) if i % 2 == 0 and c in "AEIOU"]


strs = "w3rEsOUrcE "
print("Original List:", strs)
print("Positions of all uppercase vowels (not counting Y) in even indices:")
print(test(strs))
strs = "AEIOUYW "
print("\nOriginal List:", strs)
print("Positions of all uppercase vowels (not counting Y) in even indices:")
print(test(strs))
