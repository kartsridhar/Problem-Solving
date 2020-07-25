"""
Q1.  Given a number ‘x’, and a range of ‘y’ to ‘z’. 
Find the count of all numbers ‘n’ in that range such that the product of the number ‘n’ and ‘x’ does 
not contain any digit from the number ‘n’. 

Foreg if x=2, y=11, z=13, then, 

for n=11, 2*11=22  //valid
for n=12, 2*12=24  //invalid as 24 contains 2 from n=12
for n=13, 2*13=26  //valid
"""

def solve():
    x = int(input("Enter x"))
    y = int(input("Enter y"))
    z = int(input("Enter z"))

    count = 0
    for i in range(y, z+1):
        n = list(str(i))
        prod = list(str(x*i))
        print(f'n = {n} and prod = {prod}')
        if not any(j in prod for j in n):
            count += 1
    return count

count = solve()
print(count)