# what happens if the number of elements in the list is odd

#come back to this

arr = [12, 11, 13, 5, 6, 7]

def mergeSort(arr):
    arr_pair = []
    for i in range(1, len(arr), 2):
        print(i)
        arr_pair.append([arr[i-1], arr[i]])
    
    for p in arr_pair:
        if p[1] < p[0]:
            p[0], p[1] = p[1], p[0]
    
    print(arr_pair)
    
mergeSort(arr)