"""
54. Write a Python program to remove duplicates from a list of integers, preserving order. 
Input:
[1, 3, 4, 10, 4, 1, 43]
Output:
[1, 3, 4, 10, 43]
Input:
[10, 11, 13, 23, 11, 25, 23, 76, 99]
Output:
[10, 11, 13, 23, 25, 76, 99]
Click me to see the sample solution

"""


def test(nums):
    return list(dict.fromkeys(nums))


nums = [1, 3, 4, 10, 4, 1, 43]
print("Original list of numbers:")
print(nums)
print("Remove duplicates from the said list of integers, preserving order:")
print(test(nums))
nums = [10, 11, 13, 23, 11, 25, 23, 76, 99]
print("\nOriginal list of numbers:")
print(nums)
print("Remove duplicates from the said list of integers, preserving order:")
print(test(nums))
