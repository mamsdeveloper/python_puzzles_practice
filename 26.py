"""
27. Write a Python program to find x that minimizes mean squared deviation from a given a list of numbers. 
Input:
[4, -5, 17, -9, 14, 108, -9]
Output:
17.142857142857142
Input:
[12, -2, 14, 3, -15, 10, -45, 3, 30]
Output:
1.1111111111111112
Click me to see the sample solution

"""


def test(nums):
    return sum(nums) / len(nums)


nums = [4, -5, 17, -9, 14, 108, -9]
print("Original list:")
print(nums)
print("Minimizes mean squared deviation from the said list of numbers:")
print(test(nums))
nums = [12, -2, 14, 3, -15, 10, -45, 3, 30]
print("Original list:")
print(nums)
print("Minimizes mean squared deviation from the said list of numbers:")
print(test(nums))
