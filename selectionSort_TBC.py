arr = [12,22,11,60,200]


def selectionSort(arr):
    
    n = len(arr)

    for i in range(0,n):
                
        min_num = i
        
        for k in range(i + 1, n):
            if arr[k] < arr[min_num]:
                min_num = k
                
        arr[i], arr[min_num] = arr[min_num], arr[i]
    
    return arr
         
print(selectionSort(arr))


#  the run time is O(n^2) because there is a nested for loop

# pros
# it sorting method does not require as much memonery as other methods other than cycle sort, since it only needs O(n) since
#  it is just reference the list time over and over, not changing it at all 

# cons 
#  much slower than something like quick sort or merge sort
# it is not "stable" since it does not keep the order if there are equals 

