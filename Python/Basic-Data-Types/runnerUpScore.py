if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arrNew = [i for i in arr if i != max(arr)]
    arrNew.sort(reverse=True)
    print(arrNew[0])

