
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    jawab = 0
    
    arr2 = list(arr)
             
    arr2.sort(reverse = True)
    
    for i in range(n):
        if arr2[0] > arr2[i]:
            print(arr2[i])
            break
