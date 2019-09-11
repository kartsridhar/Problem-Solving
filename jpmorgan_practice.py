s = list(str(input()))
new = s
i = 0
while i < len(new)-1 and (s[i] != "*" or s[i] != "-"):
    if int(s[i])%2 == 0 and int(s[i+1])%2 == 0:
        s.insert(i+1, '*')
        i += 1
    elif int(s[i])%2 == 1 and int(s[i+1])%2 == 1:
        s.insert(i+1, '-')
        i += 1
    i += 1
    new = s
print(''.join(new))

# 1738621831
# 1-7-38*6*2183-1