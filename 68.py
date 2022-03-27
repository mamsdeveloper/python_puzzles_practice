"""
69. Write a Python program to create a new string by taking a string, and word by word rearranging its characters in ASCII order. 
Input: Ascii character table
Output:
Aciis aaccehrrt abelt
Input: maltos won
Output:
almost now
Click me to see the sample solution

"""


def test(strs):
    return " ".join("".join(sorted(w)) for w in strs.split(' '))


strs = "Ascii character table"
print("Original string:", strs)
print("New string by said string, and word by word rearranging its characters in ASCII order:")
print(test(strs))
strs = "maltos won"
print("\nOriginal string:", strs)
print("New string by said string, and word by word rearranging its characters in ASCII order:")
print(test(strs))
