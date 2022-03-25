"""
66. Write a Python program to find the indices of the closest pair from a list of numbers. 
Input: [1, 7, 9, 2, 10]
Output:
[0, 3]
Input: [1.1, 4.25, 0.79, 1.0, 4.23]
Output:
[4, 1]
Input: [0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2]
Output:
[2, 5]
Click me to see the sample solution

"""


def test(nums):
    closest_inds = None
    closest_dist = None
    for ind, num in enumerate(nums):
        for other_ind, num2 in enumerate(nums):
            if num != num2 and ((closest_dist is None) or abs(num - num2) < closest_dist):
                closest_dist = abs(num - num2)
                closest_inds = [ind, other_ind]
                if num <= num2:
                    closest_inds = [ind, other_ind]
                else:
                    closest_inds = [other_ind, ind]
    return closest_inds


nums = [1, 7, 9, 2, 10]
print("List of numbers:", nums)
print("Indices of the closest pair from the said list of numbers:")
print(test(nums))

nums = [1.1, 4.25, 0.79, 1.0, 4.23]
print("\nList of numbers:", nums)
print("Indices of the closest pair from the said list of numbers:")
print(test(nums))
nums = [0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2]
print("\nList of numbers:", nums)
print("Indices of the closest pair from the said list of numbers:")
print(test(nums))
