"""
55. Write a Python program to find the numbers that are greater than 10 and have odd first and last digits. 
Input:
[1, 3, 79, 10, 4, 1, 39, 62]
Output:
[79, 39]
Input:
[11, 31, 77, 93, 48, 1, 57]
Output:
[11, 31, 77, 93, 57]
Click me to see the sample solution

"""


def test(nums):
    return [x for x in nums if x > 10 and x % 10 % 2 and int(str(x)[0]) % 2]


nums = [1, 3, 79, 10, 4, 1, 39]
print("Original list of numbers:")
print(nums)
print("Numbers of the said array that are greater than 10 and have odd first and last digits:")
print(test(nums))
nums = [11, 31, 77, 93, 48, 1, 57]
print("\nOriginal list of numbers:")
print(nums)
print("Numbers of the said array that are greater than 10 and have odd first and last digits:")
print(test(nums))
