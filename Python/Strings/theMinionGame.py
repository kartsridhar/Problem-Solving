def minion_game(string):
    kevin, stuart = 0, 0
    string = string.lower()
    
    for i in range(len(string)):
        if s[i] in list("AEIOU"):
            kevin += len(string - i) 
        else:
            stuart += len(string - i)
    
    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif stuart > kevin:
        print(f'Stuart {stuart}')
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)