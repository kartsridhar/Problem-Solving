# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
start = r'^hackerrank'
end = r'hackerrank$'
both = r'^(hackerrank)(.*hackerrank)?$'
pattern1 = re.compile(start)
pattern2 = re.compile(end)
pattern3 = re.compile(both)
n = int(input())
for _ in range(n):
    string = input().lower()
    if re.search(pattern3, string):
        print(str(0))
    elif re.search(pattern1, string):
        print(str(1))
    elif re.search(pattern2, string):
        print(str(2))
    else:
        print(str(-1))
