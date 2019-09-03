#Problem        : Expecto Palindronum
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

def check(data):
    return data == reversed(data)

word = data[0]

if check(word):
    print(len(word))
minimum = len(word) * 2
for i in range(len(word)//2):
    temp = word
    for j in range(len(word)):
        temp.replace(word[0], word[j])
        if check(temp):
            if len(temp) < minimum:
                minimum = len(temp)
print(minimum-1)


# #Problem        : Expecto Palindronum
# #Language       : Python 3
# #Compiled Using : py_compile
# #Version        : Python 3.4.3
# #Input for your program will be provided from STDIN
# #Print out all output from your program to STDOUT

# import sys

# data = sys.stdin.read().splitlines()

# word = list(data[0])
# c = []
# while word != word[::-1]:
#     c.append(word.pop())
# print(len(word) + len(c)*2)
