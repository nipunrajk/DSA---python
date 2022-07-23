// Maximum and minimum of an array using minimum number of comparisons

def findMinMax(arr, n):
    if (n%2 == 0):
        mn = min(arr[0], arr[1])
        mx = max(arr[0], arr[1])
        i = 2
    else:
        mn = mx = arr[0]
        i=1
    while(i<n-1):
        if (arr[i] > arr[i+1]):
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])
        else:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])

        i += 2

    print('Minimum element is', mn)
    print('Maximum element is', mx)
    return mn, mx
findMinMax([1000, 11, 445, 1, 330, 3000], 6)
