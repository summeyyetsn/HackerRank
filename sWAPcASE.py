"""
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Function Description
"""
def swap_case(s):
    new_string=""
    for char in s:
        if char.islower(): new_string+=char.upper()
        else:new_string+=char.lower()
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)