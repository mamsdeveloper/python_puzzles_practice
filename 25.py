"""
26. Write a Python program to find the largest number where commas or periods are decimal points. 
Input:
['100', '102,1', '101.1']
Output:
102.1
Click me to see the sample solution

"""


def test(str_nums):
    return max(float(s.replace(",", ".")) for s in str_nums)


str_nums = ["100", "102,1", "101.1"]
print("Original list:")
print(str_nums)
print("Largest number where commas or periods are decimal points:")
print(test(str_nums))
