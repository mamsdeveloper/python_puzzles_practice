"""
20. Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers. 
Input:
[1, 2, 3, 4, 5, 6]
Output:
Increasing.
Input:
[6, 5, 4, 3, 2, 1]
Output:
Decreasing.
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
Not a monotonic sequence!
Click me to see the sample solution

"""


def test(nums):
    return "Increasing." if all(nums[i] < nums[i + 1] for i in range(len(nums) - 1)) else \
        "Decreasing." if all(nums[i + 1] < nums[i] for i in range(len(nums) - 1)) else \
        "Not a monotonic sequence!"


nums = [1, 2, 3, 4, 5, 6]
print("Original list:")
print(nums)
print("Check the direction ('increasing' or 'decreasing') of the said list:")
print(test(nums))
nums = [6, 5, 4, 3, 2, 1]
print("\nOriginal list:")
print(nums)
print("Check the direction ('increasing' or 'decreasing') of the said list:")
print(test(nums))
nums = [19, 19, 5, 5, 5, 5, 5]
print("\nOriginal list:")
print(nums)
print("Check the direction ('increasing' or 'decreasing') of the said list:")
print(test(nums))
