"""
82. Write a Python program to find the sublist of numbers from a given list of numbers with only odd digits in increasing order. 
Input:
[1, 3, 79, 10, 4, 2, 39]
Output:
[1, 3, 39, 79]
Input:
[11, 31, 40, 68, 77, 93, 48, 1, 57]
Output:
[1, 11, 31, 57, 77, 93]
Input:
[9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
Output:
[-3, -1, 3, 9]
Click me to see the sample solution

"""


def test(nums):
    return sorted(n for n in nums if all(int(c) % 2 for c in str(abs(n))))


nums = [1, 3, 79, 10, 4, 2, 39]
print("Original list of numbers:")
print(nums)
print("Sublist of numbers of the said list with only odd digits in increasing order:")
print(test(nums))
nums = [11, 31, 40, 68, 77, 93, 48, 1, 57]
print("\nOriginal list of numbers:")
print(nums)
print("Sublist of numbers of the said list with only odd digits in increasing order:")
print(test(nums))
nums = [9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
print("\nOriginal list of numbers:")
print(nums)
print("Sublist of numbers of the said list with only odd digits in increasing order:")
print(test(nums))
