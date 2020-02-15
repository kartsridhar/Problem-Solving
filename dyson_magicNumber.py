# Input: a to b
# print all the possible magic numbers in that range
# magic number: n steps from a number, is the next number.

num = int(input())
arr = [int(x) for x in str(num)]
magic = False
step = arr[0]
for i in range(len(arr)-1):
    print(f'step = {step}')
    print(f'arr[i:(step+1)][-1] = {arr[i:(step+1)][-1]}')
    print(f'arr[i+1] = {arr[i+1]}')
    if arr[i:(step+1)][-1] == arr[i+1]:
        step = arr[(i+1)%len(arr)]
        magic = True
    else:
        print("Not a magic number")
if magic == True:
    print("It is a magic number")
else:
    print("Not a magic number")