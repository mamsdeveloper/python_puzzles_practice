"""
72. Write a Python program to find the indices of three numbers that sum to 0 in a given list of numbers. 
Input: [12, -7, 3, -89, 14, 4, -78, -1, 2, 7]
Output:
[1, 2, 5]
Input: [1, 2, 3, 4, 5, 6, -7]
Output:
[2, 3, 6]
Click me to see the sample solution

"""


def test(nums):
    # note that later duplicates will override earlier entries
    inv = {n: i for i, n in enumerate(nums)}
    for i, n in enumerate(nums):
        if inv[n] == i:
            del inv[n]
        if any((-m - n) in inv for m in nums[:i]):  # found solution!
            j, m = next((j, m) for j, m in enumerate(nums) if (-m - n) in inv)
            k = inv[-m - n]
            return sorted([i, j, k])


nums = [12, -7, 3, -89, 14, 4, -78, -1, 2, 7]

print("List of numbers:", nums)
print("Indices of three numbers that sum to 0 in the said list:")
print(test(nums))
nums = [1, 2, 3, 4, 5, 6, -7]
print("\nList of numbers:", nums)
print("Indices of three numbers that sum to 0 in the said list:")
print(test(nums))
