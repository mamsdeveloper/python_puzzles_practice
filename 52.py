"""
53. Write a Python program to find the product of the units digits in the numbers of a given list. 
Input:
[12, 23]
Output:
6
Input:
[12, 23, 43]
Output:
18
Input:
[113, 234]
Output:
12
Input:
[1002, 2005]
Output:
10
Click me to see the sample solution

"""


def test(nums):
    return eval('*'.join([str(x % 10) for x in nums]))


nums = [12, 23]
print("Original list of numbers:")
print(nums)
print("Product of the units digits in the numbers of the said:")
print(test(nums))
nums = [12, 23, 43]
print("\nOriginal list of numbers:")
print(nums)
print("Product of the units digits in the numbers of the said:")
print(test(nums))
nums = [113, 234]
print("\nOriginal list of numbers:")
print(nums)
print("Product of the units digits in the numbers of the said:")
print(test(nums))
nums = [1002, 2005]
print("\nOriginal list of numbers:")
print(nums)
print("Product of the units digits in the numbers of the said:")
print(test(nums))
