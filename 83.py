"""
84. Write a Python program to find the index of the matching parentheses for each character in a given string. 
Input: ()(())
Output:
[1, 0, 5, 4, 3, 2]
Input: ()()()
Output:
[1, 0, 3, 2, 5, 4]
Input: ((()))
Output:
[5, 4, 3, 2, 1, 0]
Click me to see the sample solution

"""


def test(parens):
    a = list(parens)
    stack = []
    for i, c in enumerate(a):
        if c == "(":
            stack.append(i)
        else:
            a[stack[-1]] = i
            a[i] = stack.pop()
    return a


parens = "()(())"
print("Original parentheses:", parens)
print("Index of the matching parentheses for each character in a given string:")
print(test(parens))
parens = "()()()"
print("\nOriginal parentheses:", parens)
print("Index of the matching parentheses for each character in a given string:")
print(test(parens))
parens = "((()))"
print("\nOriginal parentheses:", parens)
print("Index of the matching parentheses for each character in a given string:")
print(test(parens))
