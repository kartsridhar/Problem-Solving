# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = float(input())
BC = float(input())
MBC = math.degrees(math.atan((AB/2)/(BC/2)))
print(str(round(MBC)) + '°')

