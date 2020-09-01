"""
Given a string S. divide S into 2 equal parts S1 and S2. S is a halindrome if
AT LEAST one of the following conditions satisfy:

1. S is a palindrome and of length S >= 2
2. S1 is a halindrome
3. S2 is a halindrome

In case of an odd length string, S1 = [0, m-1] and S2 = [m+1, len(s)-1]

Example 1:
input: harshk
output: False

Explanation 1:
S does not form a palindrome
S1 = har which is not a halindrome
S2 = shk which is also not a halindrome.

None are true, so False.

Example 2:
input: hahshs
output: True

Explanation 2: 
S is not a palindrome
S1 = hah which is a palindrome
S2 = shs which is also a palindrome

Example 3:
input: rsrabdatekoi
output: True

Explanation 3:
rsrabd, atekoi

Neither are palindromic so you take each word and split again

Break down rsrabd coz it's not palindromic,

rsr, abd.

rsr length is >=2 and is a palindrome hence it's true
"""

def splitString(s):
    return [s[0:len(s)//2], s[len(s)//2:]] if len(s) >= 2 else []

def checkPalindrome(s):
    return s == s[::-1] if len(s) >= 2 else False

def checkHalindrome(s):
    print(s)
    if checkPalindrome(s):
        return True
    else:
        splits = splitString(s)
        if len(splits) == 0:
            return False
        else:
            for i in splits:
                return checkHalindrome(i)
        return False

inputs = 'rsrabdatekoi'
print(checkHalindrome(inputs))