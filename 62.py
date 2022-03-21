"""
63. Write a Python program to find the sum of the even elements that are at odd indices. 
Input:
[1, 2, 3, 4, 5, 6, 7]
Output:
12
Input:
[1, 2, 8, 3, 9, 4]
Output:
6
Click me to see the sample solution

"""


def test(nums):
    return sum(i for i in nums[1::2] if i % 2 == 0)


nums = [1, 2, 3, 4, 5, 6, 7]
print("Original list of numbers:")
print(nums)
print("Sum of the even elements of the said list that are at odd indices:")
print(test(nums))
nums = [1, 2, 8, 3, 9, 4]
print("\nOriginal list of numbers:")
print(nums)
print("Sum of the even elements of the said list that are at odd indices:")
print(test(nums))
