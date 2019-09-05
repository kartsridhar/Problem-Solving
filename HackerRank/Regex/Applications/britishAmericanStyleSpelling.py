# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
words = [input() for _ in range(N)] 
T = int(input())
test = [input() for _ in range(T)]

for i in range(len(test)):
    C = 0
    pattern = test[i][:-2] + '[zs]e'
    for j in range(len(words)):
        match = re.findall(pattern, words[j])
        C += len(match)
    print(C)