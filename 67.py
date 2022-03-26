"""
68. Write a Python program to find all 5's in integers less than n that are divisible by 9 or 15. 
Input:
Value of n = 50
Output:
[[15, 1], [45, 1]]
Input:
Value of n = 65
Output:
[[15, 1], [45, 1], [54, 0]]
Input:
Value of n = 75
Output:
[[15, 1], [45, 1], [54, 0]]
Input:
Value of n = 85
Output:
[[15, 1], [45, 1], [54, 0], [75, 1]]
Input:
Value of n = 150
Output:
[[15, 1], [45, 1], [54, 0], [75, 1], [105, 2], [135, 2]]
Click me to see the sample solution

"""


def test(n):
    return [[i, j] for i in range(n) for j in range(len(str(i))) if str(i)[j] == '5' and (i % 15 == 0 or i % 9 == 0)]


n = 50
print("Value of n = ", n)
print("5's in integers less than", n, "that are divisible by 9 or 15:")
print(test(n))
n = 65
print("\nValue of n = ", n)
print("5's in integers less than", n, "that are divisible by 9 or 15:")
print(test(n))
n = 75
print("\nValue of n = ", n)
print("5's in integers less than", n, "that are divisible by 9 or 15:")
print(test(n))
n = 85
print("\nValue of n = ", n)
print("5's in integers less than", n, "that are divisible by 9 or 15:")
print(test(n))
n = 150
print("\nValue of n = ", n)
print("5's in integers less than", n, "that are divisible by 9 or 15:")
print(test(n))
