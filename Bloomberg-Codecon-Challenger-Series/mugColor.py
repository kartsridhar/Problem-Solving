#Problem        : Mug Color
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()
colors = set(["White", "Black", "Blue", "Red", "Yellow"])
guesses = []
n = int(data[0])
for i in range(1, n+1):
    guesses.append(data[i])
guesses = set(guesses)
color = list(colors.difference(guesses))
print(color[0])
