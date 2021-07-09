

#Merge two sorted subsets
def merge(arr, temp, low, mid, high):
 
    k = i = low
    j = mid + 1
    inversionCount = 0
 
    # Element left and right goes
    while i <= mid and j <= high:
        if arr[i] <= (2*arr[j]):
            temp[k] = arr[i]
            i = i + 1
        else:
            temp[k] = arr[j]
            j = j + 1
            inversionCount += (mid - i + 1)
        k = k + 1
 
    #Copied the remaining elements.
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
 
    #Copy back to the original list to reflect sorted order
    for i in range(low, high + 1):
        arr[i] = temp[i]
 
    return inversionCount
 
# Sort list [low--high] using temp array
def mergeSort(arr, temp, low, high):
 
    #Base case
    if high == low:
        return 0
 
    #Find mid place
    mid = low + ((high - low) >> 1)
    inversionCount = 0
 
    #Recursively split runs into two halves until run size == 1,
    #Then merge them.
    
    #Merge left half
    inversionCount += mergeSort(arr, temp, low, mid)  
    #Merge right half      
    inversionCount += mergeSort(arr, temp, mid + 1, high)
    #Merge the two half runs
    inversionCount += merge(arr, temp, low, mid, high)
 
    return inversionCount
 
def test1():
    arr = [8, 4, 2, 1]
    temp = arr.copy()
    size = len(arr)
    print("Total number of inversions:",end=" ")
    print(mergeSort(arr, temp, 0, size - 1))
def test2():
    arr = [3,1,2]
    temp = arr.copy()
    size = len(arr)
    print("Total number of inversions:",end=" ")
    print(mergeSort(arr, temp, 0, size - 1))
    
test1()
test2()






