# -*- coding: utf-8 -*-

  
#Do insertion sort 
def insertionSort(arr, low, n): 
    for i in range(low + 1, n + 1): 
        val = arr[i] 
        j = i 
        while j>low and arr[j-1]>val: 
            arr[j]= arr[j-1] 
            j-= 1
        arr[j]= val 
  
  
# Partition function for quicksort 
def partition(arr, low, high): 
    pivot = arr[high] 
    i = low
    j = low
    for i in range(low, high): 
        if arr[i]<pivot: 
            arr[i], arr[j]= arr[j], arr[i] 
            j+= 1
    arr[j], arr[high]= arr[high], arr[j] 
    return j 
  

# QuickSort + Insertion Sort
def hybridQuickSort(arr, low, high): 
    while low<high: 
        if high-low + 1<10: 
            insertionSort(arr, low, high) 
            break
        else: 
            pivot = partition(arr, low, high) 
            #Left Side
            if pivot-low<high-pivot: 
                hybridQuickSort(arr, low, pivot-1) 
                low = pivot + 1
            else: 
                #Right side and then move left side
                hybridQuickSort(arr, pivot + 1, high) 
                high = pivot-1



def printarr(arr):
    for i in arr:
        print(i, end = " ")


arr = [9,8,3,5,6]

length = len(arr)

i = 0

hybridQuickSort(arr,i,(length-1))

print("After sorting array: ")

printarr(arr)


