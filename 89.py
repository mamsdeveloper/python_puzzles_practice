"""
90. For each triple of eaten, need, stock write a Python program to get a pair of total appetite and remaining. 
Input:
[[2, 5, 6], [3, 9, 22]]
Output:
[[7, 1], [12, 13]]
Input:
[[2, 3, 18], [4, 9, 2], [2, 5, 7], [3, 8, 12], [4, 9, 106]]
Output:
[[5, 15], [6, 0], [7, 2], [11, 4], [13, 97]]
Input:
[[1, 2, 3], [4, 5, 6]]
Output:
[[3, 1], [9, 1]]
Click me to see the sample solution

"""


def test(nums):
    return [[a+min(b, c), max(0, c-b)] for a, b, c in nums]


nums = [[2, 5, 6], [3, 9, 22]]
print("Original list (triple) of lists:")
print(nums)
print("Each triple of eaten, need, stock return a pair of total appetite and remaining:")
print(test(nums))
nums = [[2, 3, 18], [4, 9, 2], [2, 5, 7], [3, 8, 12], [4, 9, 106]]
print("\nOriginal list (triple) of lists:")
print(nums)
print("Each triple of eaten, need, stock return a pair of total appetite and remaining:")
print(test(nums))
nums = [[1, 2, 3], [4, 5, 6]]
print("\nOriginal list (triple) of lists:")
print(nums)
print("Each triple of eaten, need, stock return a pair of total appetite and remaining:")
print(test(nums))
