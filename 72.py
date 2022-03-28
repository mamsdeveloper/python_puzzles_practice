"""
73. Write a Python program to find a substring in a given string contains a vowel between two consonants. 
Input: Hello
Output:
Hel
Input: Sandwhich
Output:
San
Input: Python
Output:
hon
Click me to see the sample solution

"""


def test(s):
    cons = "bcdfghjklmnpqrstvwxz"
    vows = "aeiou"
    return next(s[i - 1:i + 2] for i in range(1, len(s) - 1)
                if s[i].lower() in vows and s[i - 1].lower() in cons and s[i + 1].lower() in cons)


strs = "Hello"
print("Original string:", strs)
print("Find a vowel between two consonants, contained in said string:")
print(test(strs))
strs = "Sandwhich"
print("\nOriginal string:", strs)
print("Find a vowel between two consonants, contained in said string:")
print(test(strs))
strs = "Python"
print("\nOriginal string:", strs)
print("Find a vowel between two consonants, contained in said string:")
print(test(strs))
