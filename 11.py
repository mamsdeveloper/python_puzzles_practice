"""
12. Write a Python program to check whether the given strings are palindromes or not. Return True, False. 
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]
Click me to see the sample solution

"""


def test(strs):
    return [s == s[::-1] for s in strs]


strs = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
print("Original strings:")
print(strs)
print("\nTest whether the given strings are palindromes or not:")
print(test(strs))
