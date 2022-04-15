"""
98. Given a string consisting of groups of matched nested parentheses separated by parentheses, write a Python program to compute the depth of each group. 
Input: (()) (()) () ((()()())) 
Output:
[2, 2, 1, 3]
Input: () (()) () () () ()
Output:
[1, 2, 1, 1, 1, 1]
Input: (((((((()))))))) () (()) ((()()()))
Output:
[8, 1, 2, 3]
Click me to see the sample solution

"""


def test(parens):
    return [len(s.split(')')[0]) for s in parens.split()]


parentheses = '(()) (()) () ((()()())) '
print("Parentheses strings:", parentheses)
print("\nDepth of groups of matched nested parentheses separated by parentheses:")
print(test(parentheses))
parentheses = '() (()) () () () ()'
print("Parentheses strings:", parentheses)
print("\nDepth of groups of matched nested parentheses separated by parentheses:")
print(test(parentheses))
parentheses = '(((((((()))))))) () (()) ((()()()))'
print("Parentheses strings:", parentheses)
print("\nDepth of groups of matched nested parentheses separated by parentheses:")
print(test(parentheses))
