"""
65. Write a Python program to shift the decimal digits n places to the left, wrapping the extra digits around. If shift > the number of digits of n, reverse the string. 
Input:
n = 12345 and shift = 1
Output:
Result = 23451
Input:
n = 12345 and shift = 2
Output:
Result = 34512
Input:
n = 12345 and shift = 3
Output:
Result = 45123
Input:
n = 12345 and shift = 5
Output:
Result = 12345
Input:
n = 12345 and shift = 6
Output:
Result = 54321
Click me to see the sample solution

"""


def test(n, shift):
    s = str(n)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]


print("Shift the decimal digits n places to the left. If shift > the number of digits of n, reverse the string.:")

n = 12345
shift = 1
print("\nn =", n, " and shift =", shift)
print("Result = ", test(n, shift))
n = 12345
shift = 2
print("\nn =", n, " and shift =", shift)
print("Result = ", test(n, shift))
n = 12345
shift = 3
print("\nn =", n, " and shift =", shift)
print("Result = ", test(n, shift))
n = 12345
shift = 5
print("\nn =", n, " and shift =", shift)
print("Result = ", test(n, shift))
n = 12345
shift = 6
print("\nn =", n, " and shift =", shift)
print("Result = ", test(n, shift))
