# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

num = r'^(\d{1,3})[ -](\d{1,3})[ -](\d{4,10})$'
pattern = re.compile(num)
n = int(input())
for _ in range(n):
    number = input()
    print('CountryCode=%s,LocalAreaCode=%s,Number=%s' % (re.match(pattern, number).groups()))
