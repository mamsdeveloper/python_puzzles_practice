"""
57. Write a Python program to find the sum of the magnitudes of the elements in the array with a sign that is equal to the product of the signs of the entries. 
Input:
[1, 3, -2]
Output:
-6
Input:
[1, -3, 3]
Output:
-7
Input:
[10, 32, 3]
Output:
45
Input:
[-25, -12, -23]
Output:
-60
Click me to see the sample solution

"""


def test(nums):
    tot = sum(abs(i) for i in nums)
    if all(nums):
        return tot if sum(i < 0 for i in nums) % 2 == 0 else -tot
    return 0


nums = [1, 3, -2]
print("Original list of numbers:")
print(nums)
print("Sum of the magnitudes of the elements in the array with a sign that is equal to the product of the signs of the entries:")
print(test(nums))
nums = [1, -3, 3]
print("\nOriginal list of numbers:")
print(nums)
print("Sum of the magnitudes of the elements in the array with a sign that is equal to the product of the signs of the entries:")
print(test(nums))
nums = [10, 32, 3]
print("\nOriginal list of numbers:")
print(nums)
print("Sum of the magnitudes of the elements in the array with a sign that is equal to the product of the signs of the entries:")
print(test(nums))
nums = [-25, -12, -23]
print("\nOriginal list of numbers:")
print(nums)
print("Sum of the magnitudes of the elements in the array with a sign that is equal to the product of the signs of the entries:")
print(test(nums))
