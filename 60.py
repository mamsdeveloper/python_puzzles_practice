"""
61. Write a Python program to find the number which when appended to the list makes the total 0. 
Input:
[1, 2, 3, 4, 5]
Output:
-15
Input:
[-1, -2, -3, -4, 5]
Output:
5
Input:
[10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]
Output:
-1316384
Click me to see the sample solution

"""


def test(nums):
    dset = set(nums)
    result = sum(nums)
    dmin = abs(min(nums) - sum(dset ^ set(nums)))
    for d in dset ^ set(nums):
        dcopy = list(nums)
        dcopy.append(d)
        ds = sum(dcopy)
        if 0-ds < dmin:
            result = ds
            dmin = abs(ds)
        elif 0-ds == dmin:
            result = min(result, ds)
    return result*(-1)


nums = [1, 2, 3, 4, 5]
print("Original list of numbers:")
print(nums)
print("Number which when appended to the list makes the total 0:")
print(test(nums))
nums = [-1, -2, -3, -4, 5]
print("\nOriginal list of numbers:")
print(nums)
print("Number which when appended to the list makes the total 0:")
print(test(nums))
nums = [10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]
print("\nOriginal list of numbers:")
print(nums)
print("Number which when appended to the list makes the total 0:")
print(test(nums))
