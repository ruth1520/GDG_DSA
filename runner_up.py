if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = sorted(arr)
    i = n-2
    while arr2[-1] == arr2[i]:
        i -= 1
    print(arr2[i])
        
