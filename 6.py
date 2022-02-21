"""
7. Write a Python program to check a given list of integers where the sum of the first i integers is i. 
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True
Input:
[2, 2, 2, 2, 2]
Output:
False
Click me to see the sample solution

"""


def test(nums):
    return all([sum(nums[:i]) == i for i in range(len(nums))])


nums = [0, 1, 2, 3, 4, 5]
print("Original list:")
print(nums)
print("Check the said list, where the sum of the first i integers is i:")
print(test(nums))
nums = [1, 1, 1, 1, 1, 1]
print("\nOriginal list:")
print(nums)
print("Check the said list, where the sum of the first i integers is i:")
print(test(nums))
nums = [2, 2, 2, 2, 2]
print("\nOriginal list:")
print(nums)
print("Check the said list, where the sum of the first i integers is i:")
print(test(nums))
