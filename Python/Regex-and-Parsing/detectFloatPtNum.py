import re
# ^ pattern at start of the string 
# $ pattern at end of the string
# [a-zA-Z0-9] = matches any letter from a-z, A-Z or 0-9
# \A only matches at the start of the string 
print(re.search(r'Ca*o*k', 'Ck').group())