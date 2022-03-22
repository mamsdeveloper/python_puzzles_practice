"""
64. Write a Python program to find the string consisting of all the words whose lengths are prime numbers. 
Input:
The quick brown fox jumps over the lazy dog.
Output:
The quick brown fox jumps the
Input:
Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later.
Output:
Omicron Effect: Foreign Flights Won't On Dec 15,
Click me to see the sample solution

"""


def test(strs):
    return " ".join(strs for strs in strs.split() if is_prime(len(strs)))


def is_prime(n):
    return n > 1 and all(n % j for j in range(2, int(n ** 0.5) + 1))


strs = "The quick brown fox jumps over the lazy dog."
print("Original list of numbers:")
print(strs)
print("Words whose lengths are prime numbers in the said string:")
print(test(strs))
strs = "Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later."
print("\nOriginal list of numbers:")
print(strs)
print("Words whose lengths are prime numbers in the said string:")
print(test(strs))
