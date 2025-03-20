#  use the word "break" to exit out of a while or for loop
# if you want to use recursion, you need to RETURN the function and not run it

arr = [64, 34, 25, 12, 22, 11, 90]




def bubbleSort(arr):
    n = len(arr)
    for k in range(n):
        for i in range(k, n-1):
            if arr[k+1] < arr[i]:
                arr[k+1], arr[i] = arr[i], arr[k+1]
    print(arr)
        
        
bubbleSort(arr)