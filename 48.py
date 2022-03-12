"""
49. Write a Python program to find the h-index, the largest positive number h such that h occurs in the sequence at least h times. If there is no such positive number return h = -1. 
Input:
[1, 2, 2, 3, 3, 4, 4, 4, 4]
Output:
4
Input:
[1, 2, 2, 3, 4, 5, 6]
Output:
2
Input:
[3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]
Output:
5
Click me to see the sample solution

"""


def test(nums):
    return max([-1] + [i for i in nums if i > 0 and nums.count(i) >= i])


nums = [1, 2, 2, 3, 3, 4, 4, 4, 4]
print("Original list of numbers:")
print(nums)
print("h-index, the largest positive number h such that h occurs in the said sequence at least h times:")
print(test(nums))
nums = [1, 2, 2, 3, 4, 5, 6]
print("\nOriginal list of numbers:")
print(nums)
print("h-index, the largest positive number h such that h occurs in the said sequence at least h times:")
print(test(nums))
nums = [3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]
print("\nOriginal list of numbers:")
print(nums)
print("h-index, the largest positive number h such that h occurs in the said sequence at least h times:")
print(test(nums))
