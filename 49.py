"""
50. Write a Python program to find the even-length words from a given list of words and sort them by length. 
Input:
['Red', 'Black', 'White', 'Green', 'Pink', 'Orange']
Output:
['Pink', 'Orange']
Input:
['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']
Output:
['!!', 'bird', 'that', 'worm', 'Absurd']
Click me to see the sample solution

"""


def test(nums):
    return sorted([w for w in words if len(w) % 2 == 0], key=lambda w: (len(w), w))


words = ["Red", "Black", "White", "Green", "Pink", "Orange"]
print("Original list of words:")
print(words)
print("Find the even-length words and sort them by length in the said list of words:")
print(test(words))
words = ['The', 'worm', 'ate', 'a', 'bird',
         'imagine', 'that', '!', 'Absurd', '!!']
print("\nOriginal list of words:")
print(words)
print("Find the even-length words and sort them by length in the said list of words:")
print(test(words))
