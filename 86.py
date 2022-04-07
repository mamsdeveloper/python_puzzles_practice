"""
87. Write a Python program to find a valid substring of a given string that contains matching brackets, at least one of which is nested. 
Input: 
]][][[]]] 
Output:
[[]]
Input: 
]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[[ 
Output:
[[][][][]]
Click me to see the sample solution

"""


def test(s):
    import re
    return re.search(r"\[(\[\])+\]", s).group(0)


brackets = "]][][[]]]"
print("Original List of strings:", brackets)
print("\nFind a valid substring of the said string that contains matching brackets, at least one of which is nested:")
print(test(brackets))
brackets = "]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[["
print("\nOriginal List of strings:", brackets)
print("\nFind a valid substring of the said string that contains matching brackets, at least one of which is nested:")
print(test(brackets))
