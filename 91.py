"""
92. Write a Python program to start with a list of integers, keep every other element in place and otherwise sort the list. 
Input: 
[2, 5, 6, 3, 1, 4, 34]
Output:
[1, 5, 2, 3, 6, 4, 34]
Input: 
[8, 0, 7, 2, 9, 4, 1, 2, 8, 3]
Output:
[1, 0, 7, 2, 8, 4, 8, 2, 9, 3]
Click me to see the sample solution

"""


def test(nums):
    li = nums.copy()
    for i in range(len(li)):
        if i % 2 == 0:
            for j in range(i+2, len(li), 2):
                if li[j] < li[i]:
                    swap(li, i, j)

    return li


def swap(li, i, j):
    temp = li[i]
    li[i] = li[j]
    li[j] = temp


nums = [2, 5, 6, 3, 1, 4, 34]
print("Original list (triple) of lists:")
print(nums)
print("In the said list, keep every other element in place and otherwise sort the list.:")
print(test(nums))
nums = [8, 0, 7, 2, 9, 4, 1, 2, 8, 3]
print("\nOriginal list (triple) of lists:")
print(nums)
print("In the said list, keep every other element in place and otherwise sort the list.:")
print(test(nums))
