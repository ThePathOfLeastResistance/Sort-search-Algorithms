#this one has a interesting way of doing it, they do 

arr = [12, 11, 13, 5, 6]


# my method
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        for k in range(i, n):
            if arr[k] < arr[i]:
                arr.insert(i, arr.pop(k))
    return arr



def insertionSorts(arr):
      for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertionSorts(arr)
print(arr)
#geeksforgeeks method 

def intserion(arr):
    for i in range(0, len(arr)):
        postion = i 
        while arr[i] < arr[i - 1] and i != 0:
            arr[i - 1] = 0 
 
print(insertionSort(arr))
            