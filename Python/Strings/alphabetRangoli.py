def print_rangoli(size):
    # your code goes here
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = list(letters)
    new_range = lambda x : list(range(x)) + list(range(x - 2, -1, -1))
    for i in new_range(size):
        rangoli = [letters[size - j - 1] for j in new_range(i+1)]
        rangoli = "-".join(rangoli)
        rangoli = rangoli.center(4*(size-1)+1, '-')
        print(rangoli)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)