# Method 1:

def reverseString(arr):
    left = 0
    right = len(arr) - 1

    while(left<right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return  arr

#Method 2:
def reverseString(arr):
    print(arr[::-1])

