# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
countries = set()
for _ in range(N):
    country = str(input())
    countries.add(country)
print(len(countries))