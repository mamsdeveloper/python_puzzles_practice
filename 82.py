"""
83. A string is happy if every three consecutive characters are distinct. Write a Python program to find two indices making a given string unhappy. 
Input: 
Python
Output:
None
Input: 
Unhappy
Output:
[4, 5]
Input: 
Find
Output:
None
Input:
Street
Output:
[3, 4]
Click me to see the sample solution

"""


def test(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 1]:
            return [i, i + 1]
        if s[i] == s[i + 2]:
            return [i, i + 2]


strs = "Python"
print("Original string:", strs)
print("Find two indices making the said string unhappy!")
print(test(strs))
strs = "Unhappy"
print("\nOriginal string:", strs)
print("Find two indices making the said string unhappy!")
print(test(strs))
strs = "Find"
print("\nOriginal string:", strs)
print("Find two indices making the said string unhappy!")
print(test(strs))
strs = "Street"
print("\nOriginal string:", strs)
print("Find two indices making the said string unhappy!")
print(test(strs))
