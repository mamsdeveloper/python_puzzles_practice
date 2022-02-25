"""
19. Write a Python program to split a given string (s) into strings if there is a space in the string, otherwise split on commas if there is a comma, otherwise return the list of lowercase letters with odd order (order of a = 0, b = 1, etc.) 
Input:
a b c d
Split the said string into strings if there is a space in the string, 
otherwise split on commas if there is a comma, 
Output:
['a', 'b', 'c', 'd']
Input:
a,b,c,d
Split the said string into strings if there is a space in the string, 
otherwise split on commas if there is a comma, 
Output:
['a', 'b', 'c', 'd']
Input:
abcd
Split the said string into strings if there is a space in the string, 
otherwise split on commas if there is a comma,
Output:
['b', 'd']
Click me to see the sample solution

"""


def test(s):
    if " " in s:
        return s.split(" ")
    if "," in s:
        return s.split(",")
    return [c for c in s if c.islower() and ord(c) % 2 == 0]


strs = "a b c d"
print("Original string:")
print(strs)
print("Split the said string into strings if there is a space in the string, \notherwise split on commas if there is a comma, \notherwise return the list of lowercase letters with odd order:")
print(test(strs))
strs = "a,b,c,d"
print("\nOriginal string:")
print(strs)
print("Split the said string into strings if there is a space in the string, \notherwise split on commas if there is a comma, \notherwise return the list of lowercase letters with odd order:")
print(test(strs))
strs = "abcd"
print("\nOriginal string:")
print(strs)
print("Split the said string into strings if there is a space in the string, \notherwise split on commas if there is a comma, \notherwise return the list of lowercase letters with odd order:")
print(test(strs))
