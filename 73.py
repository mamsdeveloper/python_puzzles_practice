"""
74. Write a Python program to find a string consisting of space-separated characters with given counts. 
Input: {'f': 1, 'o': 2}
Output:
f o o
Input: {'a': 1, 'b': 1, 'c': 1}
Output:
a b c
Click me to see the sample solution

"""


def test(counts):
    return " ".join(c for c, i in counts.items() for _ in range(i))


strs = {"f": 1, "o": 2}
print("Original string:", strs)
print("String consisting of space-separated characters with given counts:")
print(test(strs))
strs = {"a": 1, "b": 1, "c": 1}
print("\nOriginal string:", strs)
print("String consisting of space-separated characters with given counts:")
print(test(strs))
