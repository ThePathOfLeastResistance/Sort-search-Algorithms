arr = [2, 3, 4, 10, 40]
input = input("input the number here:")

def binarySearch(arr, input):
    n = len(arr)
    middle_num = int(n//2)
    print(arr)
    middle = arr[middle_num]
    if middle > int(input):
        arr = arr[0: middle_num]
    elif middle < int(input):
        arr = arr[middle_num: n]
    else:
        return print(f"right number at index {middle_num}")
        
    return binarySearch(arr, input)

binarySearch(arr, input)