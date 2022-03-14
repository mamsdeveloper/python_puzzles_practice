"""
52. Write a Python program to reverse the case of all strings. For those strings, which contain no letters, reverse the strings. 
Input:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Output:
['CAT', 'CATATATATCTSA', 'ABCDEFHIJKLMNOP', '521581932952421', '', 'FOO', 'UNIQUE']
Input:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Output:
['gREEN', 'rED', 'oRANGE', 'yELLOW', '', 'wHITE']
Input:
['Hello', '[email protected]#', '[email protected]#$', '123#@!']
Output:
['hELLO', '[email protected]#', '[email protected]#$', '123#@!']
Click me to see the sample solution

"""


def test(strs):
    return [s[::-1] if s.isdigit() else s.swapcase() for s in strs]


strs = ['cat', 'catatatatctsa', 'abcdefhijklmnop',
        '124259239185125', '', 'foo', 'unique']
print("Original list:")
print(strs)
print("Reverse the case of all strings. For those strings which contain no letters, reverse the strings:")
print(test(strs))
strs = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
print("\nOriginal list:")
print(strs)
print("Reverse the case of all strings. For those strings which contain no letters, reverse the strings:")
print(test(strs))
strs = ["Hello", "[email protected]#", "[email protected]#$", "123#@!"]
print("\nOriginal list:")
print(strs)
print("Reverse the case of all strings. For those strings which contain no letters, reverse the strings:")
print(test(strs))
