"""
80. Write a Python program to round each float in a given list of number up to the next integer and return the running total of the integer squares. 
Input: [2.6, 3.5, 6.7, 2.3, 5.6]
Output:
[9, 25, 74, 83, 119]
Input: [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]
Output:
[91204, 252808, 253337, 183714223444221, 183714327525025, 283714327525025]
Click me to see the sample solution

"""


def test(nums):
    from math import ceil
    running_squares = []
    tot = 0
    for v in nums:
        tot += ceil(v) ** 2
        running_squares.append(tot)
    return running_squares


nums = [2.6, 3.5, 6.7, 2.3, 5.6]
print("List of numbers:", nums)
print("Round each float of the said list up to the next integer and return the running total of the integer squares:")
print(test(nums))
nums = [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]
print("\nList of numbers:", nums)
print("Round each float of the said list up to the next integer and return the running total of the integer squares:")
print(test(nums))
