"""
46. Given an array of numbers representing a branch on a binary tree, write a Python program to find the minimum even value and its index. In the case of a tie, return the smallest index. If there are no even numbers, the answer is []. 
Input:
[1, 9, 4, 6, 10, 11, 14, 8]
Output:
Minimum even value and its index of the said array of numbers:
[4, 2]
Input:
[1, 7, 4, 4, 9, 2]
Output:
Minimum even value and its index of the said array of numbers:
[2, 5]
Input:
[1, 7, 7, 5, 9]
Output:
Minimum even value and its index of the said array of numbers:
[]
Click me to see the sample solution

"""


def test(nums):
    if any(n % 2 == 0 for n in nums):
        return min([v, i] for i, v in enumerate(nums) if v % 2 == 0)
    else:
        return []


nums = [1, 9, 4, 6, 10, 11, 14, 8]
print("Original list:")
print(nums)
print("Minimum even value and its index of the said array of numbers:")
print(test(nums))
nums = [1, 7, 4, 4, 9, 2]
print("Original list:")
print(nums)
print("Minimum even value and its index of the said array of numbers:")
print(test(nums))
nums = [1, 7, 7, 5, 9]
print("Original list:")
print(nums)
print("Minimum even value and its index of the said array of numbers:")
print(test(nums))
