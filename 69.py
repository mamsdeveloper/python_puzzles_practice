"""
70. Write a Python program to find the first negative balance from a given a list of numbers which represent bank deposits and withdrawals. 
Input:
[[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]
Output:
[-81, -1]
Input:
[[1200, 100, -900], [100, 100, -2400]]
Output:
[None, -2200]
Click me to see the sample solution

"""


def test(balances):
    firsts = []
    for bals in balances:
        total = 0
        for b in bals:
            total += b
            if total < 0:
                firsts.append(total)
                break
        else:
            firsts.append(None)
    return firsts


balances = [[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]
print("Bank deposits and withdrawals:")
print(balances)
print("\nFirst negative balance of deposits and withdrawals:")
print(test(balances))
balances = [[1200, 100, -900], [100, 100, -2400]]
print("Bank deposits and withdrawals:")
print(balances)
print("\nFirst negative balance of deposits and withdrawals:")
print(test(balances))
