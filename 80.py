"""
81. Write a Python program to calculate the average of the numbers a through b ( b not included ) rounded to nearest integer, in binary (or -1 if there are no such numbers). 
Input: 
4 , 7
Output:
0b101
Input:
11 , 19
Output:
0b1110
Click me to see the sample solution

"""


def test(a, b):
    r = range(a, b)
    if len(r) == 0:
        return "-1"
    return bin(round(sum(r) / len(r)))


a = 4
b = 7
print("Range:", a, ",", b)
print("Average of the numbers", a, "through", b,
      "rounded to nearest integer, in binary:")
print(test(a, b))
a = 11
b = 19
print("\nRange:", a, ",", b)
print("Average of the numbers", a, "through", b,
      "rounded to nearest integer, in binary:")
print(test(a, b))
