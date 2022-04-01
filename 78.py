"""
79. Write a Python program to find the largest negative and smallest positive numbers (or 0 if none). 
Input: 
[-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
Output:
[-6, 2]
Input: 
[-1, -2, -3, -4]
Output:
[-1, 0]
Input: 
[1, 2, 3, 4]
Output:
[0, 1]
Input:
[]
Output:
[0, 0]
Click me to see the sample solution

"""


def test(nums):
    pos = [n for n in nums if n > 0]
    neg = [n for n in nums if n < 0]
    return [max(neg) if neg else 0, min(pos) if pos else 0]


nums = [-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
print("List of numbers:", nums)
print("Largest negative and smallest positive numbers (or 0 if none) of the said list:")
print(test(nums))
nums = [-1, -2, -3, -4]
print("\nList of numbers:", nums)
print("Largest negative and smallest positive numbers (or 0 if none) of the said list:")
print(test(nums))
nums = [1, 2, 3, 4]
print("\nList of numbers:", nums)
print("Largest negative and smallest positive numbers (or 0 if none) of the said list:")
print(test(nums))
nums = []
print("\nList of numbers:", nums)
print("Largest negative and smallest positive numbers (or 0 if none) of the said list:")
print(test(nums))
