"""
40. Write a Python program to find string s that, when case is flipped gives target where vowels are replaced by chars two later. 
Input: Python
Output:
pYTHQN
Input: aeiou
Output:
CGKQW
Input: Hello, world!
Output:
hGLLQ, WQRLD!
Input: AEIOU 
Output:
cgkqw
Click me to see the sample solution

"""


def test(strs):
    return strs.translate({ord(c): ord(c)+2 for c in "aeiouAEIOU"}).swapcase()


strs = "Python"
print("Original string:", strs)
print("Find string s that, when case is flipped gives target where vowels are replaced by chars two later:")
print(test(strs))
strs = "aeiou"
print("\nOriginal string:", strs)
print("Find string s that, when case is flipped gives target where vowels are replaced by chars two later:")
print(test(strs))
strs = "Hello, world!"
print("\nOriginal string:", strs)
print("Find string s that, when case is flipped gives target where vowels are replaced by chars two later:")
print(test(strs))
strs = "AEIOU"
print("\nOriginal string:", strs)
print("Find string s that, when case is flipped gives target where vowels are replaced by chars two later:")
print(test(strs))
