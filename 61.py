"""
62. Write a Python program to find the dictionary key whose case is different than all other keys. 
Input:
{'red': '', 'GREEN': '', 'blue': 'orange'}
Output:
GREEN
Input:
{'RED': '', 'GREEN': '', 'orange': '#125GD'}
Output:
orange
Click me to see the sample solution

"""


def test(dict_data):
    for different in dict_data:
        if all(k.islower() != different.islower() for k in dict_data if k != different):
            return different


dict_data = {"red": "", "GREEN": "", "blue": "orange"}
print("Original dictionary key-values:")
print(dict_data)
print("Find the dictionary key whose case is different than all other keys:")
print(test(dict_data))
dict_data = {"RED": "", "GREEN": "", "orange": "#125GD"}
print("\nOriginal dictionary key-values:")
print(dict_data)
print("Find the dictionary key whose case is different than all other keys:")
print(test(dict_data))
