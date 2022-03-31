"""
75. Write a Python program to reorder numbers from a give array in increasing/decreasing order based on whether the first plus last element is odd/even. 
Reorder numbers of a give array in increasing/decreasing order based on whether the first plus last element is odd/even.:
Input:
[3, 7, 4]
Output:
[3, 4, 7]
Input: 
[2, 7, 4]
Output:
[7, 4, 2]
Input: 
[1, 5, 6, 7, 4, 2, 8] 
Output:
[1, 2, 4, 5, 6, 7, 8]
Input: 
[1, 5, 6, 7, 4, 2, 9]
Output:
[9, 7, 6, 5, 4, 2, 1]
Click me to see the sample solution

"""


def test(nums):
    return sorted(nums, reverse=(False if (nums[0] + nums[-1]) % 2 else True))


print("Reorder numbers of a give array in increasing/decreasing order based on whether the first plus last element is odd/even.:")
nums = [3, 7, 4]
print("\nList of numbers:", nums)
print("Result:")
print(test(nums))
nums = [2, 7, 4]
print("\nList of numbers:", nums)
print("Result:")
print(test(nums))
nums = [1, 5, 6, 7, 4, 2, 8]
print("\nList of numbers:", nums)
print("Result:")
print(test(nums))
nums = [1, 5, 6, 7, 4, 2, 9]
print("\nList of numbers:", nums)
print("Result:")
print(test(nums))
