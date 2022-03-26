"""
67. Write a Python program to find a string which, when each character is shifted (ASCII incremented) by shift, gives the result. 
Input:
Ascii character table
Shift = 1
Output:
@rbhhbg`q`bsdqs`akd
Input:
Ascii character table
Shift = -1
Output:
Btdjj!dibsbdufs!ubcmf
Click me to see the sample solution

"""


def test(strs, shift):
    return "".join(chr(ord(c) - shift) for c in strs)


strs = "Ascii character table"
print("Original string:")
print(strs)
shift = 1
print('Shift =', shift)
print("A new string which, when each character is shifted (ASCII incremented) by shift in the said string:")
print(test(strs, shift))
strs = "Ascii character table"
print("\nOriginal string:")
print(strs)
shift = -1
print('Shift =', shift)
print("A new string which, when each character is shifted (ASCII incremented) by shift in the said string:")
print(test(strs, shift))
