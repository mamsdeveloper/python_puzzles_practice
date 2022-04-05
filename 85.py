"""
86. Write a Python program to find the vowels from each of the original texts (y counts as a vowel at the end of the word) from a given list of strings. 
Input: ['w3resource', 'Python', 'Java', 'C++']
Output:
['eoue', 'o', 'aa', '']
Input: ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
Output:
['ay', 'auy', 'aeeay', 'aaey', 'aoeey']
Click me to see the sample solution

"""


def test(strs):
    return ["".join(c for c in text if c.lower() in "aeiou") + (text[-1] if text[-1].lower() == "y" else "")
            for text in strs]


strs = ["w3resource", "Python", "Java", "C++"]
print("Original List of strings:", strs)
print("Vowels from each of the original texts (y counts as a vowel at the end of the word:")
print(test(strs))
strs = ["ably", "abruptly", "abecedary", "apparently", "acknowledgedly"]
print("\nOriginal List of strings:", strs)
print("Positions of all uppercase vowels (not counting Y) in even indices:")
print(test(strs))
