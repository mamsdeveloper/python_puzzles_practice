"""
88. Write a Python program to find an integer (n >= 0) with the given number of even and odd digits. 
Input: 
Number of even digits: 2 ,Number of odd digits: 3
Output:
22333
Input: 
Number of even digits: 4 ,Number of odd digits: 7
Output:
22223333333
Click me to see the sample solution

"""


def test(a, b):
    return int(evens*"2"+odds*"3")


evens = 2
odds = 3
print("Number of even digits:", evens, ",Number of odd digits:", odds)
print("Integer(>= 0) with the given number of even and odd digits:")
print(test(evens, odds))
evens = 4
odds = 7
print("\nNumber of even digits:", evens, ",Number of odd digits:", odds)
print("Integer(>= 0) with the given number of even and odd digits:")
print(test(evens, odds))
