"""
58. Write a Python program to find the biggest even number between two numbers inclusive. 
Input:
m = 12
n = 51
Output:
50
Input:
m = 1
n = 79
Output:
78
Input:
m = 47
n = 53
Output:
52
Input:
m = 100
n = 200
Output:
200
Click me to see the sample solution

"""


def test(m, n):
    if m > n or (m == n and m % 2 == 1):
        return -1
    return n if n % 2 == 0 else n - 1


m = 12
n = 51
print("\nBiggest even number between", m, "and", n)
print(test(m, n))
m = 1
n = 79
print("\nBiggest even number between", m, "and", n)
print(test(m, n))
m = 47
n = 53
print("\nBiggest even number between", m, "and", n)
print(test(m, n))
m = 100
n = 200
print("\nBiggest even number between", m, "and", n)
print(test(m, n))
