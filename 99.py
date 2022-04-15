"""
100. Write a Python program to find four positive even integers whose sum is a given integer. 
Input:
n = 100
Output:
[94, 2, 2, 2]
Input:
n = 1000
Output:
[994, 2, 2, 2]
Input:
n = 10000
Output:
[9994, 2, 2, 2]
Input:
n = 1234567890
Output:
[1234567884, 2, 2, 2]
Click me to see the sample solution

"""


def test(n):
    for a in range(n, 0, -1):
        if not a % 2 == 0:
            continue
        for b in range(n - a, 0, -1):
            if not b % 2 == 0:
                continue
            for c in range(n - b - a, 0, -1):
                if not c % 2 == 0:
                    continue
                for d in range(n - b - c - a, 0, -1):
                    if not d % 2 == 0:
                        continue
                    if a + b + c + d == n:
                        return [a, b, c, d]


n = 100
print("Four positive even integers whose sum is", n)
print(test(n))
n = 1000
print("\nFour positive even integers whose sum is", n)
print(test(n))
n = 10000
print("\nFour positive even integers whose sum is", n)
print(test(n))
n = 1234567890
print("\nFour positive even integers whose sum is", n)
print(test(n))
