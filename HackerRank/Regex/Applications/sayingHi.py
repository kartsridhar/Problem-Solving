# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for i in range(n):
    s = str(input())
    regex_pattern = re.compile(r'^[hH][iI]\s[^dD].*')
    if regex_pattern.match(s):
        print(s)
