"""
36. Write a Python program to find the largest k numbers from a given list of numbers. 
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5, 5]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5, 5, 4]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5, 5, 4, 3]
Click me to see the sample solution

"""


def test(nums, k):
    if k == 0:
        return []
    return sorted(nums, reverse=True)[:k]


nums = [1, 2, 3, 4, 5, 5, 3, 6, 2]
print("Original list of numbers:", nums)
k = 1
print("Largest", k, "numbers from the said list:")
print(test(nums, k))
k = 2
print("Largest", k, "numbers from the said list:")
print(test(nums, k))
k = 3
print("Largest", k, "numbers from the said list:")
print(test(nums, k))
k = 4
print("Largest", k, "numbers from the said list:")
print(test(nums, k))
k = 5
print("Largest", k, "numbers from the said list:")
print(test(nums, k))
