
import math 
  
#Fills lookup array lookup[][] in bottom up attitude.  
def solve(arr, size): 
  
    #Initialize for te intervals
    for i in range(0, size):  
        temp[i][0] = arr[i]  
        
    j = 1
      
    #Calculated the values from small to large.
    while (1 << j) <= size:  
  
        #Calculated the minimum value for all ranges with size 2 ^ j.
        i = 0
        while (i + (1 << j) - 1) < size:  
            if (temp[i][j - 1] < temp[i + (1 << (j - 1))][j - 1]):  
                temp[i][j] = temp[i][j - 1]  
            else: 
                temp[i][j] = temp[i + (1 << (j - 1))][j - 1]  
              
            i = i + 1
        j = j+ 1
  
#Return minimum of arr  
def query(left, right):  
  
    #Found the maximum power of 2 which is less than or equal to the number of elements in the given range.
    j = int(math.log2(right - left + 1))  

    if temp[left][j] <= temp[right - (1 << j) + 1][j]:  
        return temp[left][j]
    else: 
        return temp[right - (1 << j) + 1][j]
if __name__ == "__main__": 
    arr = [3,5,9,4]  
    size = len(arr)  
    MAX = 10
          
    #temp[i][j] will store min value in arr, should be using nlogn.
    temp = [[0 for i in range(MAX)] 
                 for j in range(MAX)] 
  
    solve(arr, size)  
    intervals = [query(0,1),query(0,2),query(1,3),query(2,3)]
    
    print("Every internal all values minimum:",end="\n")
    for i in intervals:
        print(i)