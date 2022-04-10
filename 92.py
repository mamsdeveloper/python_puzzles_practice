"""
93. Write a Python program to find the closest palindrome from a given string. 
Input: 
cat
Output:
cac
Input: 
madan
Output:
madam
Input: 
radivider
Output:
radividar
Input: 
madan
Output:
madam
Input:
abc
Output:
aba
Input:
racecbr
Output:
racecar
Click me to see the sample solution

"""


def test(s):
    odd = 0
    for i, c in enumerate(s):
        if c != s[~i]:
            odd += 1
    if odd % 2 == 1:
        half = odd // 2
        pal = "".join((s[i] if i < half else s[~i] for i in range(len(s))))
        return pal
    else:
        half = odd // 2
        pal = "".join((s[i] if i <= half else s[~i] for i in range(len(s))))
        return pal


s = "cat"
print("Original string:", s)
print("Closest palindrome of the said string:")
print(test(s))
s = "madan"
print("\nOriginal string:", s)
print("Closest palindrome of the said string:")
print(test(s))
s = "radivider"
print("Original string:", s)
print("Closest palindrome of the said string:")
print(test(s))
s = "madan"
print("\nOriginal string:", s)
print("Closest palindrome of the said string:")
print(test(s))
s = "abc"
print("Original string:", s)
print("Closest palindrome of the said string:")
print(test(s))
s = "racecbr"
print("\nOriginal string:", s)
print("Closest palindrome of the said string:")
print(test(s))
