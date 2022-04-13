"""
96. Write a Python program to get the single digits in numbers sorted backwards and converted to English words. 
Input: 
[1, 3, 4, 5, 11]
Output:
['five', 'four', 'three', 'one']
Input: 
[27, 3, 8, 5, 1, 31]
Output:
['eight', 'five', 'three', 'one']
Click me to see the sample solution

"""


def test(nums):
    digits = {"zero": None,
              "one": 1,
              "two": 2,
              "three": 3,
              "four": 4,
              "five": 5,
              "six": 6,
              "seven": 7,
              "eight": 8,
              "nine": 9}
    digits_backwards = {digits[k]: k for k in digits}
    digits = [digits[s] for s in digits]
    li = [digits[n] for n in nums if n in digits]
    return [digits_backwards[n] for n in sorted(li, reverse=True)]


nums = [1, 3, 4, 5, 11]
print("Original list of numbers:")
print(nums)
print("Return the single digits in nums sorted backwards and converted to English words:")
print(test(nums))
nums = [27, 3, 8, 5, 1, 31]
print("\nOriginal list of numbers:")
print(nums)
print("Return the single digits in nums sorted backwards and converted to English words:")
print(test(nums))
