def minion_game(string):
    kevin, stuart = 0, 0
    string = string.lower()
    substrings = []
    for i in range(len(string)): 
        for j in range(i+1,len(string)+1): 
            substrings.append(s[i:j])
    
    for i in substrings:
        i = list(i)
        if i[0] in list("AEIOU"):
            kevin += 1
        else:
            stuart += 1
    
    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif stuart > kevin:
        print(f'Stuart {stuart}')
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)