"""
71. Given a list of numbers and a number to inject, write a Python program to create a list containing that number in between each pair of adjacent numbers. 
Input: [12, -7, 3, -89, 14, 88, -78, -1, 2, 7]
Separator: 6
Output:
[12, 6, -7, 6, 3, 6, -89, 6, 14, 6, 88, 6, -78, 6, -1, 6, 2, 6, 7]
Input: [1, 2, 3, 4, 5, 6]
Separator: 9
Output:
[1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6]
Click me to see the sample solution

"""


def test(nums, sep):
    ans = [sep] * (2 * len(nums) - 1)
    ans[::2] = nums
    return ans


nums = [12, -7, 3, -89, 14, 88, -78, -1, 2, 7]
separator = 6
print("List of numbers:", nums)
print("Separator:", separator)
print("Inject the separator in between each pair of adjacent numbers of the said list:")
print(test(nums, separator))
nums = [1, 2, 3, 4, 5, 6]
separator = 9
print("\nList of numbers:", nums)
print("Separator:", separator)
print("Inject the separator in between each pair of adjacent numbers of the said list:")
print(test(nums, separator))
