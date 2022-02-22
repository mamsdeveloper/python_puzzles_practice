"""
15. Write a Python program find the longest string of a given list of strings. 
Input:
['cat', 'car', 'fear', 'center']
Output:
center
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
shatter
Click me to see the sample solution

"""


def test(words):
    return max(words, key=len)


strs = ['cat', 'car', 'fear', 'center']
print("Original strings:")
print(strs)
print("Longest string of the said list of strings:")
print(test(strs))
strs = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print("\nOriginal strings:")
print(strs)
print("Longest string of the said list of strings:")
print(test(strs))
