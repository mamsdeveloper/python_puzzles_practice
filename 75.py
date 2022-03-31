"""
76. Write a Python program to find the index of the largest prime in the list and the sum of its digits. 
Input: [3, 7, 4] 
Output:
[1, 7]
Input: [3, 11, 7, 17, 19, 4] 
Output:
[4, 10]
Input: [23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]
Output:
[6, 7]
Click me to see the sample solution

"""


def test(nums):
    n, i = max((n, i) for i, n in enumerate(nums) if is_prime(n))
    return [i, sum(int(c) for c in str(n))]


def is_prime(n):
    return n > 1 and all(n % j for j in range(2, int(n ** 0.5) + 1))


nums = [3, 7, 4]
print("List of numbers:", nums)
print("Index of the largest prime in the said list and the sum of its digits:")
print(test(nums))
nums = [3, 11, 7, 17, 19, 4]
print("\nList of numbers:", nums)
print("Index of the largest prime in the said list and the sum of its digits:")
print(test(nums))
nums = [23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]
print("\nList of numbers:", nums)
print("Index of the largest prime in the said list and the sum of its digits:")
print(test(nums))
