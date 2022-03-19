"""
59. A valid filename should end in .txt, .exe, .jpg, .png, or .dll, and should have at most three digits, no additional periods. Write a Python program to create a list of True/False that determine whether candidate filename is valid or not. 
Input:
['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
Output:
['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes']
Input:
['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java']
Output:
['No', 'Yes', 'No', 'No', 'No']
Click me to see the sample solution

"""


def test(file_names):
    return ["Yes" if
            f.split(".")[1:] in [['txt'], ['png'], ['dll'], ['exe'], [
                'jpg']] and f[0].isalpha() and sum(c.isdigit() for c in f) < 4
            else "No"
            for f in file_names]


file_names = ['abc.txt', 'windows.dll',
              'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
print("Original list of files:")
print(file_names)
print("Valid filenames:")
print(test(file_names))
file_names = ['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java']
print("\nOriginal list of files:")
print(file_names)
print("Valid filenames:")
print(test(file_names))
